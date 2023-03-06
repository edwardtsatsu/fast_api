from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql.schema import Column

from src.config.db import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))
    created_on = Column(DateTime)
