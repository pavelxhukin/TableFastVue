from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

message = "hello from main.py"

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class LessonBase(BaseModel):
    subject_name: str
    
class RoomBase(BaseModel):
    room_number: int
    lessons: List[LessonBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/send")
async def send_message():
    return "RMQ message is sent!"

@app.get("/table")
async def get_table(db: db_dependency):
    result = db.query(models.Lessons).all()
    if not result:
        raise HTTPException(status_code=404, detail='there is no lessons in db')
    return result

@app.get("/rooms")
async def get_room(db: db_dependency):
    result = db.query(models.Rooms).all()
    if not result:
        raise HTTPException(status_code=404, detail='there is no rooms in db')
    return result


@app.post("/table")
async def create_table(room: RoomBase, db: db_dependency):
    db_room = models.Rooms(room_number=room.room_number)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    for lesson in room.lessons:
        db_lesson = models.Lessons(subject_name=lesson.subject_name, room_id=db_room.id)
        db.add(db_lesson)
    db.commit()