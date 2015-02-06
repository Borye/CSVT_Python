import MySQLdb

class MysqlCtrl(object):
	def __init__(self, dbname = 'test', 
		         hostname = '127.0.0.1', 
		         username = 'root', 
		         por = 3306):
		self.conn = MySQLdb.connect(host = hostname, user = username, port = por)
		self.conn.select_db(dbname)
		self.cur = self.conn.cursor()

	def insert(self, id, name, age):
		sqli = 'insert into info value(%s, %s, %s)'
		self.cur.execute(sqli, (id, name, age))
		self.conn.commit()

	def __del__(self):
		self.cur.close()
		self.conn.close()

if __name__ == "__main__":
	mm = MysqlCtrl()