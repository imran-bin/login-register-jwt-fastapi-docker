from fastapi import APIRouter,Depends,HTTPException  
from sqlalchemy.orm import Session 
from app.schemas.user_schema import UserCreate,UserLogin 
from app.services.user_service import UserService 
from app.dependencies.db import get_db 

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        service = UserService(db)
        service.register(user.email, user.password)
        return {"message": "User registered"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        service = UserService(db)
        token = service.login(user.email, user.password)
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
