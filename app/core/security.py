from passlib.context import CryptContext
from jose import jwt 
SECRECT_KEY = "SECRECT0397"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"])
class SecurityService:
    @staticmethod
    def hash_password(password:str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password,hashed):
        return pwd_context.verify(password,hashed)
    @staticmethod
    def create_token(data:dict):
         expire = datetime.utcnow()+timedelta(minutes=30)
         data.update({"exp":expire})
         return jwt.encode(data,SECRECT_KEY,algorithm=ALGORITHM)

