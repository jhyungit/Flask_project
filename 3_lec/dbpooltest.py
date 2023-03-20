from mysql.connector import  pooling



pool= pooling.MySQLConnectionPool(pool_name = "mypool",pool_reset_session=True,
                              pool_size = 3, host='localhost',port='3306',
                              database='flaskdb',user='root', password='go759623fl')

# con = pool.get_connection()
# c = con.cursor()
# c.execute('insert into student values(%s,%s,%s)',('이순신',50,'1989-05-12'))
# con.commit()
# print(c.rowcount)
# con.close()

'''
con = pool.get_connection()
c1 = con.cursor()
# c.execute('select * from student')
# c.fetchall()
c1.callproc('selectProc')

for result in c1.stored_results():
    print(result.fetchall())
    print('-' * 30)
con.close()
'''

con = pool.get_connection()
c2 = con.cursor()
c2.callproc('insertProc', ('마이프록', 60, '1999-12-11'))
print(c2.rowcount)
con.close()