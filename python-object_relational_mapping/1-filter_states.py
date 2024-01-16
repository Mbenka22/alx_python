"""write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv

# Check if correct number of arguments is provided
if len(sys.argv) != 4:
    print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    sys.exit(1)

# Retrieve command line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Establish a connection to MySQL server
conn = MySQLdb.connect(host="localhost", port=3006, user=mysql_username, passwd=mysql_password, db=database_name)

# Create a cursor
cursor = conn.cursor()

# Execute SQL query to select states starting with 'N'
sql_query = """
    SELECT * FROM states
    WHERE name LIKE 'N%'
    ORDER BY states.id;
"""


cursor.execute(sql_query)


results = cursor.fetchall()
for row in results:
    print(row)


cursor.close()
conn.close()
