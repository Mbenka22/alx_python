'''Module to be imported'''
'''Module to be imported'''

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class State(Base):
    '''State class'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)

    # def __repr__(self):
    #     return f"({self.id} {self.name})"

# # SQLite import and connection string
# engine = create_engine('sqlite:///mydb.hbtn_0e_6_usa', echo=True)

# # Create the table
# Base.metadata.create_all(bind=engine)

# # Create a session
# Session = sessionmaker(bind=engine)
# session = Session()

# # #adding a state to the database
# # new_state = State(name="New York")
# # session.add(new_state)
# # session.commit()
