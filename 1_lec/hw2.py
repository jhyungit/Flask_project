from flask import Flask, render_template ,request 
import sys

app = Flask(__name__)


@app.route("/hw2")
def hw2():
    return render_template('hw2.html')   



if __name__ =="__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)
    # 웹서버 구동... requests 처리