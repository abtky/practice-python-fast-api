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

def delete_task(db: Session, id: int):
    target = db.query(models.Task).filter_by(id=id).first()
    db.delete(target)
    db.commit()
    return id