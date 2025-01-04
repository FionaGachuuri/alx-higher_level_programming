#!/usr/bin/python3
"""
Lists all cities of a state from the database `hbtn_0e_4_usa`.
Usage: ./5-filter_cities.py <mysql username>
<mysql password> <database name> <state name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
