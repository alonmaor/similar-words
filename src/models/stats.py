from sqlalchemy import Column, Integer
from sqlalchemy.types import Date
from database import Base

class Request(Base):
    __tablename__ = "Requests"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    duration = Column(Integer)