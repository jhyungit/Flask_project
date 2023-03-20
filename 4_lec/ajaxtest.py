from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/ajaxForm')
def ajaxForm():
    return render_template('ajaxForm.html')

@app.route('/ajaxHTML')
def ajaxHTML():
    return render_template('ajaxHTML.html')

@app.route('/travel')
def travel_html():
    return render_template('travel.html')

@app.route('/main')
def main_html():
    return render_template('main.html')

@app.route('/thai')
def thai_html():
    return render_template('thai.html')

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)