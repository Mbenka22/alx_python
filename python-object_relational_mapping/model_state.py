"""importing various models to work with orm such as sqlalchemy such as creati_engine and the object state"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name

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
