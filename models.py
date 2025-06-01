from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Base declaration
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = 'scholars'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, index=True)
    email = Column(String(55))
    grade = Column(Integer)
    birthday = Column(DateTime)
    enrolled_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Student {self.id}: {self.name}, Grade {self.grade}>"
