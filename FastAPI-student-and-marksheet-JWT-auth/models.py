from database_connection import base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
class studentModel(base):
    __tablename__="student"
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    marksheets = relationship("markssheetModel", back_populates="student")
    
class markssheetModel(base):
    __tablename__="marksheet"
    id=Column(Integer, primary_key=True,index=True)
    stud_id = Column(Integer, ForeignKey('student.id'))
    marks=Column(Integer)
    student = relationship("studentModel", back_populates="marksheets")
    