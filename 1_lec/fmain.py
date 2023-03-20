from flask import Flask, render_template ,request 
import sys



app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>hello flask</h1>" #response

@app.route("/test")
def test():
    return "<h1>test flask</h1>" #response

@app.route("/aa")
def aa():
    return render_template('a.html')

@app.route("/div")
def div():
    return render_template('div.html')

@app.route("/img")
def img():
    return render_template('img.html')

@app.route("/anchor")
def anchor():
    return render_template('anchor.html')

@app.route("/ul")
def ul():
    return render_template('ul.html')   

@app.route("/table")
def table():
    return render_template('table.html')    

@app.route("/form")
def form():
    return render_template('form.html')   

@app.route("/formproc")
def formproc():
    print(request.args)
    myname = request.args['myname']
    myage = request.args['myage']
    return render_template('formproc.html',myname=myname ,myage=myage,
                        test='hello')
    #return f"<h1>이름:{myname} 나이:{myage}</h1>"

@app.route("/quiz")
def quiz():
    return render_template('quiz.html') 

@app.route("/quizproc")
def quizproc():
    # print(request.args)
    num1 = int(request.args['num1'])
    num2 = int(request.args['num2'])
    # return render_template('formporc.html')
    return f"<h1>합은:{num1+num2}</h1>"

@app.route("/bimanform")
def quibimanformz():
    return render_template('bimanform.html')


@app.route("/bmiproc")
def bmiproc():
    height = int(request.arg[height])
    weight = int(request.arg[weight])
    result,picture =calcBMI (height,weight)

@app.route("/imageChangeForm")
def imageChangeForm():
    return render_template('imageChangeForm.html')
   

    
    return render_template('bmiproc.html' , height =height, weight=weight , result=result ,picture=picture)


if __name__ =="__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)
    # 웹서버 구동... requests 처리

