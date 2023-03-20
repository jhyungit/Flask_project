from mysql.connector import connect

def insertStudent(name, age, birth):
    try:
        sql = "insert into student values(%s, %s, %s)" #mysql은 무조건 %s
        conn = connect(host = 'localhost', user = 'root', password = 'go759623fl',
        db = 'flaskdb', charset = 'utf8')
        cur = conn.cursor()
        # cur.execute(sql, ('이순신', 30, '1989-02-03'))
        cur.execute(sql, (name, age, birth))
        print(cur.rowcount) # 개수세기
        conn.commit()
        conn.close()
        print('추가 성공')

    except Exception as err:
        print('실패', err)

def selectStudent():
    try:
        sql = "select * from student" #mysql은 무조건 %s
        conn = connect(host = 'localhost', user = 'root', password = 'go759623fl',
                    db = 'flaskdb', charset = 'utf8')
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        conn.close()
        print(data)
        for n, a, b in data:
            print(n, a, b)
    except Exception as err:
        print('실패', err)