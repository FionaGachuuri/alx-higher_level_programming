#!/usr/bin/python3
"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    state_name = sys.argv[4]

    db = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=sys.argv[1]
        passwd=sys.argv[2]
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY "{}" "
                   .format(sys.argv[4]))
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
