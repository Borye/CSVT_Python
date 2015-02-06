from mysqlctrl import MysqlCtrl

id = input('Please input your id: ')
name = raw_input('Please input your name: ')
age = input('Please input your age: ')

print id, name, age

mm = MysqlCtrl('pythoner')
mm.insert(id, name, age)