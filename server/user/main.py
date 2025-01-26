import json
from jose import JWTError, jwt
from database import SessionLocal, Base
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import *
from config import connection_params
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated, Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

class UserCreate(BaseModel):
    username: str
    userpassword: str
    group_id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenAuth(BaseModel):
    token: str

def tokenDecode(token: str):
    response = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = response.get("sub")
    return username

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/auth/")
def auth(db: db_dependency, token: TokenAuth):
    result = tokenDecode(token.token)
    if not result:
        raise HTTPException(status_code=401,detail="nothing")
    user = get_user(db, result)
    if user.token != token.token:
        raise HTTPException(status_code=401,detail="nothing")
    return {"username":result}



#----------------------------------------------- API -----------------------------------------------#
def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(db, data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    username = data.get("sub")
    user = get_user(db, username)
    expire = datetime.now(timezone.utc) + (timedelta(minutes=300), expires_delta)[bool(expires_delta)]
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    user.token = encoded_jwt
    print(user.token)
    print("hi")
    db.commit()
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@app.post("/register", response_model=Token)
async def register(user: UserCreate, db: db_dependency):
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_new_password = get_password_hash(user.userpassword)
    db_user = User(username=user.username, hashed_password=hashed_new_password, group_id=user.group_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token = create_access_token(db, data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/token", response_model=Token)
async def login_for_access_token(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(db, data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


    
    
