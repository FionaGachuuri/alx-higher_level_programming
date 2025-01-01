#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states, sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all the rows from the query result
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
