"""write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb
# from sys import argv
# mysql_username=argv[1]
# mysql_password=argv[2]
# db_name=argv[3]

connect= MySQLdb.connect(host='localhost', user='mirriam', passwd='florence2024#', db='hbtn_0e_0_usa', port=3006)
cursor=connect.cursor()
create_table_query=("CREATE TABLE IF NOT EXISTS states (id  INT NOT NULL AUTO-INCREMENT), name VARCHAR(256) NOT NULL, PRIMARY KEY(id)")
cursor.execute(create_table_query)
insert_data_query = "INSERT INTO states (name) VALUES (%s),(%s),(%s),(%s),(%s)"
data_values = ('California', 'Arizona', 'Texas', 'New York', 'Nevada')
