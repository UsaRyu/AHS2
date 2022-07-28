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
            text= '日本では「平和」を意味するサインとして写真を撮る時の定番ポーズです。ですが、海外では勝利(Victory)を表すVサインであったり、ギリシャでは「くたばれ」という意味であったりします。(ギリシャでは、昔、犯罪者に二本指でモノを投げつけた習慣から侮辱的な意味合いになったそうです。)'
            ref= '参考文献：https://www.keisen.ac.jp/seminar/2022/03/post-265.html　https://livejapan.com/ja/article-a0002154/　https://news.j-wave.co.jp/2017/03/ng-6.html'
        elif result == 'shaka_hang':
            result = 'シャカ/ハングル―ス'
            text= 'ハワイで使われる「アロハ（ALOHA）」にはポーズがあり、それがこのハンドサインです。「アロハ―」と言いながら笑顔でこのポーズを取れは完璧だそうです。手の向きのよって呼び方や意味が異なり、手のひらを相手に見せると「ハングルース（hang loose）」と呼び、こんにちは、ありがとう、またね、気楽にいこうなどの意味があります。逆に、相手に手の甲を見せると「シャカ（shaka）」と呼び、元気？　大丈夫？　頑張ろう！　などの意味があります。'
            ref= '参考文献：https://news.arukikata.co.jp/column/travel-info/Hawaii/Hawaii/other_cities_in_Hawaii/146_323031_1576136940.html'
        elif result =='thumbs_up':
            result = 'サムズアップ'
            text= '親指を立てるサムズアップは、ヒッチハイクや「いいね！」という意味でよく知られています。アメリカなどでは「Good!」という肯定の意味で使われるハンドサインです。しかしアフガニスタン、イラン、イタリアの一部、ギリシャなどでは「くそくらえ」というような相手を侮辱する意味と取られることがあるので、注意が必要です。'
            ref= '参考文献：https://livejapan.com/ja/article-a0002154/'
        return render_template('result.html', score=int(score*100),result=result, img_path=img_path, text=text, ref=ref)

@app.route('/about') # http://○○○/item-listを実行した場合にこの関数が実行される
def about():
    return render_template('about.html')

@app.route('/dictionary') # http://○○○/item-listを実行した場合にこの関数が実行される
def dic():
    return render_template('dictionary.html')

if __name__ == "__main__":
    app.run(debug=True)