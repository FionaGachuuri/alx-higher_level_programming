#!/usr/bin/python3
"""
Module that  lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve states starting with 'N'
    query = """
    SELECT id, name
    FROM states
    WHERE nme LIKE 'N%'
    ORDER BY id ASC
    """
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
