
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Annotated, Optional, Dict
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import *
import models
#----#
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
# Schemas
from pydantic import BaseModel
from http_client import RpcClient



models.Base.metadata.create_all(bind=engine)
class GroupCreate(BaseModel):
    description: str

class UserCreate(BaseModel):
    username: str
    userpassword: str
    group_id: int


class ScheduleCreate(BaseModel):
    weekday: WeekdayEnum
    time: str
    title: str
    cabinet: str
    group_id: int



app = FastAPI()
rpc_client = RpcClient()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/add_group/")
def add_group(group: GroupCreate, db: Session = Depends(get_db)):
    new_group = Group(description=group.description)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    
    return {"message": "Группа добавлена", "group_id": new_group.id}


@app.post("/add_schedule/")
def add_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    new_schedule = Schedule(
        time=schedule.time,
        title=schedule.title,
        cabinet=schedule.cabinet,
        weekday=schedule.weekday,
        group_id=schedule.group_id
    )
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    
    return {"message": "Занятие добавлено"}


@app.get("/get_schedule_by_group/{group_id}")
def get_schedule_by_group(group_id: int, db: Session = Depends(get_db)):
    schedules = db.query(Schedule).filter(Schedule.group_id == group_id).all()
    return {"group_id": group_id, "schedules": schedules}



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


    
class ScheduleGet(BaseModel):
    id: int
    title: str
    description: str
    
# Authentication setup
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
db_dependency = Annotated[Session, Depends(get_db)]

async def get_current_user(db: db_dependency, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username = rpc_client.call(token)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(db, username)
    if user is None:
        raise credentials_exception
    return user


def get_user(db, username: str):
    return db.query(User).filter(User.username == username).first()


user_dependency = Annotated[dict, Depends(get_current_user)]


@app.get("/tables/")
def return_tables(db: db_dependency, current_user: user_dependency):
    tables = db.query(Schedule).filter(Schedule.group_id == current_user.group_id).all()
    return tables

@app.get("/user/")
def return_user_name(db: db_dependency, current_user: user_dependency):
    return {"username":current_user.username}

@app.get("/exit/")
def return_exit(db: db_dependency, current_user: user_dependency):
    current_user.token = None
    db.commit()
    
    return {"exit":True}

@app.get("/enums/")
def get_enums():
    return {"days": [item.value for item in WeekdayEnum], "timeSlots":[item.value for item in TimeSlots]}


