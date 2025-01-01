#!/usr/bin/python3
"""
Module that  lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",  # MySQL server is on the same machine
        port=3306,         # MySQL default port
        user=sys.argv[1],  # First argument: MySQL username
        passwd=sys.argv[2],  # Second argument: MySQL password
        db=sys.argv[3]     # Third argument: Database name
    )

    # Cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve states starting with 'N'
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
