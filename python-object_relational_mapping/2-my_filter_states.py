import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    # statename_searched = input("enter state name:  ")
    

    connect = MySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql_password, port=3006, db=db_name)
    cursor = connect.cursor()
    sql_query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connect.close()