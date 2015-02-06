#coding:utf8
'''
数据库： 增删改查

MySQLdb

conn = MySQLdb.connect() 连接数据库，创建链接对象
conn.select_db(dbname) 选择数据库
cursor = conn.cursor()  创建游标对象

cursor.execute('SQL')
cursor.executemany('SQL')
cursor.fetchone()
cursor.fetchmany(size)
cursor.scroll(location, mode)

rollback()
callproc(self, procname, args):
nextset(self)

'''

import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', port = 3306)
conn.select_db('pythoner')
cur = conn.cursor()

## add
cur.execute("insert into info value(9, 'test', 90)")

## look
cur.execute("select * from info;")
cur.fetchone()  # look one row
cur.fetchall()  # look all the rows
cur.scroll(0, mode = "absolute")  # scroll to up

## before end
conn.commit()
cur.close()
conn.close()