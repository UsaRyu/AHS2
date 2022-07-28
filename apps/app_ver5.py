import os
import sys 
from flask import (
     Flask, 
     request, 
     render_template)
#import pandas as pd
from output import predict

UPLOAD_FOLDER='./static/hand_image'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        #print(upload_file)
        img_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
        #img_path = UPLOAD_FOLDER + '/' upload_file.filename
        upload_file.save(img_path)
        result, score = predict(img_path)
        if result == 'corna':
            result = 'コルナ'
            text= 'コルナは人差し指と小指を上に出し、中の指を手のひらに向けて曲げるジェスチャーです。ハードロックバンドやそのファンは過去数十年にわたって、これを承認や喜びの象徴としてきたそうです。多くのヨーロッパの国では悪魔の印でされる一方、ヒンドゥー教や仏教では肯定的なサインとされています。イタリア、ブラジル、キューバ、スペイン、ポルトガルでは、配偶者が浮気をしていることを示すために使われます。'
            ref = '参考文献：https://englishlive.ef.com/ja-jp/blog/study-tips/hand-gestures/'
        elif result == 'peace':
            result = 'ピース'
            text = '日本では「平和」を意味するサインとして写真を撮る時の定番ポーズです。ですが、海外では勝利(Victory)を表すVサインであったり、ギリシャでは「くたばれ」という意味であったりします。(ギリシャでは、昔、犯罪者に二本指でモノを投げつけた習慣から侮辱的な意味合いになったそうです。)'
            ref = '参考文献：Wikipedia'
        elif result == 'shaka_hang':
            result = 'シャカ/ハングル―ス'
            text = '別名でメロイック・サインとも呼ばれ、ヘヴィメタルやロックで有名なハンドサインです。悪運や邪視を祓う意味もあるほか、サタンやサタン崇拝とも関連性があるらしいです。地中海諸国では侮辱的な意味を持つので注意。'
            ref = '参考文献：Wikipedia'
        elif result =='thumbs_up':
            result = 'サムズアップ'
            text = '別名でメロイック・サインとも呼ばれ、ヘヴィメタルやロックで有名なハンドサインです。悪運や邪視を祓う意味もあるほか、サタンやサタン崇拝とも関連性があるらしいです。地中海諸国では侮辱的な意味を持つので注意。'
            ref = '参考文献：Wikipedia'
        return render_template('result.html', score=int(score*100),result=result, img_path=img_path, text=text, ref=ref)

if __name__ == "__main__":
    app.run(debug=True)