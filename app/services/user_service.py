from sqlalchemy.orm import SessionLocal
from models.user import User
from core.security import SecurityService

class UserService:
    def __init__(self,db:Session):
        self.db= db 
    def register(self,email:str,password:str):
        user=self.db.query(User).filter(User.email == email).first()
        if user: 
            raise ValueError("user already exists")
        new_user = User(email=email,password=SecurityService.hash_password(password))
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user 

    def login(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise ValueError("Invalid credentials")

        if not SecurityService.verify_password(password, user.password):
            raise ValueError("Invalid credentials")

        return SecurityService.create_token({"sub": user.email})