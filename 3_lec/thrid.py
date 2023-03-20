from flask import Flask, render_template,request
from mysql.connector import connect

from flask_paginate import Pagination, get_page_args
import pandas as pd
import dbhandle as d
import dbhandlePool as p
# from dbhandle import insertStudentDB

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>hello</h1>"

@app.route('/insertProc')
def insertProc():
    myname = request.args['myname']
    myage = int(request.args['myage'])
    mybirth = request.args['mybirth']
    result = d.insertProdcutDB(myname, myage, mybirth)
    # result = insertStudentDB(myname, myage, mybirth)
    return render_template('insertProc.html', result = result)

@app.route('/insertStudent')
def insertStudent():
    return render_template('insertStudent.html')

@app.route("/select")
def select():
    data = d.selectStudent()
    return render_template('selectView.html', data = data)


@app.route("/deleteView")
def deleteForm():
    return render_template('deleteView.html')

@app.route('/deleteProc')
def deleteProc():
    myname = request.args['myname']
    result = d.deleteStudent(myname)
    return render_template('insertProc.html', result = result)

@app.route('/dbhandlePool')
def dbhandlePool():
    myname = request.args['myname']
    myage = int(request.args['myage'])
    mybirth = request.args['mybirth']
    result = p.insertStudentPool(myname, myage, mybirth)
    return render_template('insertProc.html', result = result)

@app.route('/births')
def births():
    birth = pd.read_csv('births.csv', header = None)
    print(birth.values.tolist())
    return render_template('birthView.html', birth = birth.values.tolist())

birth = pd.read_csv('births.csv', header = None)
birthlist = birth.values.tolist()

def get_birth(offset = 0, per_page = 10):
    return birthlist[offset:offset+per_page]

@app.route('/birthsPage')
def birthsPage():
    page, per_page, offset = get_page_args(page_parameter = 'page',
                        per_page_parameter = 'per_page')
                        
    print('-' * 30)
    print('page:', page, 'per_page:', per_page, 'offset:', offset)
    print('-' * 30)

    total = len(birthlist)
    pagination_births = get_birth(offset = offset , per_page = per_page)
    pagination = Pagination(page = page, per_page = per_page, total = total,
                    css_framework = 'bootstrap5')
    return render_template('birthViewPage.html', births = pagination_births,
                        pagination = pagination)

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)
    # 웹서버 구동... requests 처리