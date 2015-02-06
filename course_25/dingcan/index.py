#coding:utf8
import MySQLdb

TEMPLATE_DIR = 'C:\\Apache24\\htdocs\\dingcan\\templates\\'

def get_template(tmpname):
    fp = open(TEMPLATE_DIR + tmpname, 'r')
    html = fp.read()
    fp.close()
    return html


def application(environ, start_response):
    status = '200 ok'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)

    conn = MySQLdb.connect(host = '127.0.0.1', 
                           user = 'root', 
                           port = 3306, 
                           db = 'db_3')
    cur = conn.cursor()
    sql = 'select * from menu'
    cur.execute(sql)
    rs = cur.fetchall()
    print(rs)
    out = ''
    for r in rs:
      out += '%s %s %s <br/>'%r

    cur.close()
    conn.close()

    html = get_template('index.tpl')

    return [bytes(html%out, 'utf8')]

