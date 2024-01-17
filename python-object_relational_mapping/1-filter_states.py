import MySQLdb
from sys import argv

if __name__ == '__main__':  # Note the double underscores in __name_

    MySql_username = argv[1]
    MySql_password = argv[2]
    db_name = argv[3]

    connect= MySQLdb.connect(host='localhost', passwd=MySql_password, port=3006, user=MySql_username, db=db_name)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM states WHERE BINARY LEFT(name, 1) = "N" ORDER BY id ASC')
    '''This query will select the name column from the table where the first letter of the name is a capital 'N'.
      The BINARY keyword is used to perform a case-sensitive comparison.'''
    rows = cursor.fetchall()

    for row in rows:
        print(row) 

    cursor.close()
    connect.close()