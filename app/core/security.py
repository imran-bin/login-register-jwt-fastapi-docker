from passlib.context import CryptContext
from jose import jwt 
from datetime import datetime, timedelta
import os

SECRET_KEY = os.getenv("SECRET_KEY", "SECRET0397")
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"])
class SecurityService:
    @staticmethod
    def hash_password(password:str):
        return pwd_context.hash(password[:72])

    @staticmethod
    def verify_password(password,hashed):
        return pwd_context.verify(password[:72],hashed)
    @staticmethod
    def create_token(data:dict):
         expire = datetime.utcnow()+timedelta(minutes=30)
         data.update({"exp":expire})
         return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

