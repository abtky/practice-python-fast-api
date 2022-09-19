from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import crud
from db.database import SessionLocal

router = APIRouter()

class Task(BaseModel):
    id: int
    label: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/task")
async def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db, 30)

@router.post("/task/")
async def add_task(label: str, db:Session = Depends(get_db)):
    return crud.create_task(db, label)
