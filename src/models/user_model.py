from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from src.config.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password
