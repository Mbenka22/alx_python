"Trunctate"
import MySQLdb
from sys import argv
mysql_username=argv(1)
mysql_password=argv(2)
db_name=argv(3)

connect=MySQLdb.connect(
    host='localhost',
    user=mysql_username,
    passwd=mysql_password, 
    database=db_name, 
    port=3006)

cursor=connect.cursor()
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
cursor.execute(query)


cursor.close
connect.close

