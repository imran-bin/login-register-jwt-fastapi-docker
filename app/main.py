from fastapi import FastAPI 
from app.core.database import Base,engine 
from app.routers.auth_routers import router as auth_router 

Base.metadata.create_all(bind=engine) 
app =FastAPI()
app.include_router(auth_router)
