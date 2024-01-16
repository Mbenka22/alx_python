"""a script that takes in an arguement and dispalys all the values in the states table"""
import mySQLdb
from sys import argv
mysql_username=argv(1)
mysql_password=argv(2)
db_name=argv(3)
state_name=argv(4)
if __name__=='__main__':
    connect=mySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql_password, databse=db_name,port=3006)
    cursor=connect.cursor()
    sql_query="SELECT *FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_query(state_name,))
    results=cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connect.close()    