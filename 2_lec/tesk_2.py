from flask import Flask, render_template,request

app = Flask(__name__)

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
