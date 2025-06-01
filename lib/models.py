import os
import sys

# Ensure Python can find this file if imported elsewhere
sys.path.append(os.getcwd())

from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, DateTime
)
from sqlalchemy.ext.declarative import declarative_base

# Create engine that points to your SQLite DB
engine = create_engine('sqlite:///migrations_test.db')

# Define the declarative base
Base = declarative_base()

# Define your Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return f"<Student {self.id}: {self.name}, Grade {self.grade}>"
