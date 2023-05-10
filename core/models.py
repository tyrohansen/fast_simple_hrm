from sqlalchemy import TIMESTAMP, Column, Date, ForeignKey, Integer, String
from sqlalchemy.sql import func
from core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    user_employees = relationship("Employee", back_populates="author")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    department = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    id_no = Column(String, nullable=False)
    nin = Column(String, nullable=False)
    date_joined = Column(Date)
    marital_status = Column(String, nullable=False)
    birth_place = Column(String, nullable=False)
    residence = Column(String, nullable=False)
    birth_date = Column(Date)
    kin_name = Column(String, nullable=False)
    kin_contact = Column(String, nullable=False)
    emergency_contact = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    author = relationship("User", back_populates="user_employees")