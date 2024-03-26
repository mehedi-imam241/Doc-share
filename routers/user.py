import bcrypt
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from database import get_db
from schemas.Response.Response import Response

load_dotenv()

from utils.hash import hash_password
from utils.JWT_util import getJWT

from schemas.Response.User import User as UserResponse
from schemas.Request.UserCreate import UserCreate
from schemas.Request.UserLogin import UserLoginPayload
from schemas.Response.UserLoginResponse import UserLoginResponse

from models.User import User

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/signup/", response_model=Response)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        return {"message": "User already exists", "success": False}

    hashed_password = hash_password(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully", "success": True}


@router.post("/login/", response_model=UserLoginResponse)
def login_user(payload: UserLoginPayload, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()

    if not user:
        return {"message": "User not found", "success": False}
    if not bcrypt.checkpw(payload.password.encode(), user.hashed_password.encode()):
        return {"message": "Incorrect password", "success": False}

    jwt_token = getJWT(user)
    return {"token": jwt_token, "user": user, "message": "Login successful"}
