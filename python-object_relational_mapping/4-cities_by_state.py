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
cursor = connect.cursor()
cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id=states.id
        ORDER BY cities.id ASC;
        """)
for row in cursor:
    print(row)
cursor.close()
connect.close()