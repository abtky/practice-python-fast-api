from fastapi import FastAPI, Depends, Query
from typing import Optional
from pydantic import BaseModel
from fastapi.testclient import TestClient

from db.fake_db import fake_item_db, fake_tasks_db
from sqlalchemy.orm import Session
from db import crud, models
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}   

class Task(BaseModel):
    id: int
    label: str
    

@app.get("/task/")
async def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db, 30)

@app.post("/task/")
async def add_task(label: str, db:Session=Depends(get_db)):
    return crud.create_task(db, label)

@app.get("/items/")
async def read_items():
    return fake_item_db

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    elm = filter(lambda x: x['id'] == item_id, fake_item_db)
    return { "item_id": item_id }

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    return item