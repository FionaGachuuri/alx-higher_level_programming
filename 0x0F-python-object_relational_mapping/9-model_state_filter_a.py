#!/usr/bin/python3
"""
The script lists all State objects
that contain t letter `a`,
from  database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and get a state
    from it.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))
