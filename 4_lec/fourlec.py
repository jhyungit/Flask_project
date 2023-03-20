from flask import Flask, render_template,request
from mysql.connector import  pooling
from base64 import b64encode
import pandas as pd
import plotly
import plotly.express as px
import json

pool= pooling.MySQLConnectionPool(pool_name = "mypool",pool_reset_session=True,
                              pool_size = 3, host='localhost',port='3306',
                              database='flaskdb',user='root', password='go759623fl')
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/fileForm')
def fileForm():
    return render_template('fileForm.html')

@app.route('/fileSend', methods = ['POST'])
def fileSend():
    # myname = request.form['myname']
    # myfile = request.files['myfile']
    # print(myname)
    # print(myfile.filename)
    # myfile.save(f'rfile/{myfile.filename}')

    myfile = request.files['myfile']
    sql = 'insert into imgup(fname, imgfile) values(%s, %s)'
    con = pool.get_connection()
    c = con.cursor()
    c.execute(sql, (myfile.filename, myfile.read()) )
    con.commit()
    print(c.rowcount)
    con.close()
    return '<h1>db insert</h1>'

@app.route('/selectImg')
def selectImg():
    con = pool.get_connection()
    c = con.cursor()
    c.execute('select * from imgup')
    result = c.fetchall()
    # web image --> base64 encoding(string)
    # data = []
    # for n, img in result:
    #     b = b64encode(img).decode('utf-8')
    #     data.append((n, 'data:;base64,'+b))

    con.close()
    return render_template('selectImg.html', data = result)

# https://tedboy.github.io/jinja2/templ14.html
@app.route('/myFilter')
def myFilter():
    return render_template('myFilter.html', n = -10, f = 3.141592,
        s = 'abc', s1 = '   def   ')

@app.template_filter('reverse') # 사용자 정의 필터
def reverse_filter(s):
    return s[-1::-1]

@app.template_filter('base64')
def base64_filter(img):
    b = b64encode(img).decode('utf-8')
    return 'data:;base64,' + b

@app.route('/selectStudent')
def selectStudent():
    con = pool.get_connection()
    c = con.cursor()
    c.execute('select * from student')
    result = c.fetchall()
    con.close()
    return render_template('selectStudent.html', data = result)

@app.template_filter('strftime')
def strftime(b):
    return b.strftime('%Y년%m월%d일')

@app.route('/studentChart')
def studentChart():
    sql = 'select * from student'
    df = pd.read_sql(sql, pool.get_connection())

    fig = px.bar(df, x="name", y="age", title="타이틀", width=600, height=400,
                 labels={'NAME':'이름','AGE':'나이'},
                 color_discrete_map={"나이": "RebeccaPurple"},
                 template="simple_white",text='age')
    fig.update_layout(yaxis_range=[0,100])

    graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

    return render_template('nodash.html', graphJSON = graphJSON)

@app.route('/barChart')
def barChart():
    df = pd.read_csv('births.csv',header=None)
    df.columns = ['year', 'boy', 'girl']
    my_df = df[df['year']>=2000]

    fig = px.bar(my_df, x = 'year', y='boy', title="타이틀", width=600, height=400,
                 labels={'year':'년도','boy':'남아수'},
                 color_discrete_map={"년도": "RebeccaPurple"},
                 template="simple_white",
                 text='boy')

    graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

    return render_template('nodash.html', graphJSON = graphJSON)

@app.route('/meltChart')
def meltChart():
    df = pd.read_csv('births.csv',header=None)
    df.columns = ['year', 'boy', 'girl']
    my_df = df[df['year']>=2000]
    
    my_df = pd.melt(my_df, id_vars=['year'], var_name= 'gender', value_name='value')
    fig = px.bar(my_df, x = 'year', y = 'value', color = 'gender',
    barmode = 'group', text = 'value')
    fig.show()

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)