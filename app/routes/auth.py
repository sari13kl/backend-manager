from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import sessionmaker
from app.core.config import Settings
from app.database.session import get_db
from app.database.models.user import User
from app.schemas.user import CreateSchema, LoginSchema
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("")
async def home():
    return {"message": "Auth Home"}

def create_access_token():
    pass  # Implement JWT token creation logic here

def authenticate_user():
    pass  # Implement user authentication logic here



@auth_router.post("/register", response_model=CreateSchema)
def register_user():
    pass  # Implement user registration logic here

@auth_router.post("/login")
def login_user():
    pass  # Implement user login logic here



    

