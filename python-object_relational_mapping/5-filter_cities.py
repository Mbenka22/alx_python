# from sqlalchemy import create_engine, ForeignKey,column, String,INTEGER,CHAR
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()
import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_passwd = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    connect = MySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql_passwd, port=3306, db=db_name)
    cursor = connect.cursor()
    sql_query = """SELECT cities.name
               FROM cities
               INNER JOIN states ON
               cities.state_id=states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC
                """
    cursor.execute(sql_query, (state_name,))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cursor.close()
    connect.close()