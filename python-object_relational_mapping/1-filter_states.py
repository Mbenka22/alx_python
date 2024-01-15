"""write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv
mysql_username=argv[1]
mysql_password=argv[2]
db_name=argv[3]

connect = MySQLdb.connect(
        host='localhost', user=mysql_username, passwd=mysql_password,
        database=db_name, port=3006)
cursor=connect.cursor()
