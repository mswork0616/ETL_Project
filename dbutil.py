# dbutil.py
 
import pymysql
 
def getConnect():
    conn = pymysql.connect(host='localhost',
    port=3306, db='playdata', user='bigdata', password='bigdata', charset='utf8')
    return conn
 
print(getConnect())
 

