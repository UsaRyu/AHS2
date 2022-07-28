import os
from flask import Flask, render_template, request,url_for

from calculation import trapezoid_area

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calc",methods=["GET","POST"])
def calculation():
    if request.method == "GET":
        return render_template('calculation.html')
    elif request.method == "POST":
        top = request.form['top']
        bottom = request.form['bottom']
        height = request.form['height']
        area = trapezoid_area(top, bottom, height)
        if isinstance(area, (int,float)) == True: #整数以外の入力を受け付けない
            #isinstance 関数は 1 番目の引数に指定したオブジェクトが 2 番目の引数に指定したデータ型と等しいかどうかを返します
            return render_template('calculation.html', area=area)
        else:
            return render_template("calculation.html", error=area)

#Flaskで静的ファイルを更新で反映させるために以下を記載
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == "__main__":
    app.run(debug=True)