from typing import Union
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import task
from app.utils import get_db

router = APIRouter()

class Task(BaseModel):
    id: Union[int, None] = None
    label: str

@router.get("/task")
async def read_tasks(db: Session = Depends(get_db)):
    return task.get_tasks(db, 30)

@router.post("/task")
async def add_task(task: Task, db:Session = Depends(get_db)):
    return task.create_task(db, task.label)

@router.delete("/task/{taskId}")
async def remove_task(taskId: int, db:Session = Depends(get_db)):
    return task.delete_task(db, taskId)