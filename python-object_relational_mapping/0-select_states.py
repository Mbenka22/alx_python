""""this script connects to MYSQL server,
list all state from the database hbtn_0e_0_usa, it takes 3 argument"""
import MySQLdb
from sys import argv
mysql_username=argv[1]
mysql_password=argv[2]
db_name=argv[3]

connect = MySQLdb.connect(
        host='localhost', user=mysql_username, passwd=mysql_password,
        database=db_name, port=3006)


cursor = connect.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)
for row in cursor:
    print(row)
cursor.close()
connect.close()

