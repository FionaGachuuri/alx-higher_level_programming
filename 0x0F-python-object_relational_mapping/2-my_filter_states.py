#!/usr/bin/python3
"""Filter states by user input from the database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cur = db.cursor()

    # SQL query with user input
    query = """SELECT * FROM states WHERE name = '{}'
    ORDER BY id ASC""".format(state_name)

    # Execute the query
    cur.execute(query)

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
