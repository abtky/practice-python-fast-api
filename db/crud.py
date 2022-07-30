from sqlalchemy.orm import Session
import datetime
from . import models

def get_tasks(db: Session, limit: int = 20):
    return db.query(models.Task).limit(limit).all()

def create_task(db: Session, label: str):
    task = models.Task(label = label, created_at = datetime.datetime.now())
    db.add(task)
    db.commit()
    db.refresh(task)
    return label