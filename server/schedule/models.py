from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(Integer, index=True)

class Lessons(Base): 
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))