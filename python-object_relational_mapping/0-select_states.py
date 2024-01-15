from sys import argv
import MySQLdb

def list_states(username, password, database_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost', port=3006, user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        # Execute the SQL query to select all states
        query = "SELECT * FROM states ORDER BY id;"
        cursor.execute(query)

        # Fetch all the results
        states = cursor.fetchall()

        # Print the list of states
        print("List of States:")
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to the database: {e}")
    finally:
        # Close the database connection
        if db:
            db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        # Extract MySQL credentials from command line arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Call the function to list states
        list_states(mysql_username, mysql_password, database_name)
