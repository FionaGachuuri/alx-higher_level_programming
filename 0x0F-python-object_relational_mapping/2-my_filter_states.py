#!/usr/bin/python3
"""
Module where an argument is taken  and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to find states matching the state_name
    query = """
    SELECT id, name
    FROM states
    WHERE name LIKE BINARY %s
    ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
