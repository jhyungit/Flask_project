from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>hello flask</h1>" #r    esponse

@app.route("/jinjaIf")
def jinjaif():
    return render_template('jinjaif.html',num=10)

@app.route("/jinjaFor")
def jinjaFor():
    return render_template('jinjaFor.html', myList = ['사과', '딸기', '포도', '수박']) 

@app.route("/formTest")
def formTest():
    return render_template('formTest.html')

@app.route("/formProc")
def formProc():
    myname = request.args['myname']
    myage = request.args['myage']
    mybirth = request.args['mybirth']
    color = request.args['color']
    hobby = request.args.getlist('hobby')
    print(hobby)
    hobby = '-'.join(hobby)
    return render_template('formProc.html', myname = myname, myage = myage, mybirth = mybirth, color = color, hobby = hobby)

@app.route("/bootTest")
def bootTest():
    return render_template('bootTest.html')

@app.route("/travel")
def travel():
    return render_template('travel.html')

@app.route("/phi")
def phi():
    return render_template('phi.html')

@app.route("/thai")
def thai():
    return render_template('thai.html')

@app.route("/tesk_2")
def tesk_2():
    return render_template('tesk_2.html')

@app.route("/tesk_2proc")
def tesk_2proc():
    myname = request.args['myname']
    mytel = request.args['mytel']
    myemail = request.args['myemail']
    size = request.args['size']
    topping = request.args.getlist('topping')
    deltime = request.args['deltime']
    delrequst = request.args['delrequst']
    topping = '-'.join(topping)
    return render_template('tesk_2proc.html', myname = myname, mytel = mytel, myemail = myemail, size = size, topping = topping,
    deltime = deltime, delrequst = delrequst)

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)
    # 웹서버 구동... requests 처리