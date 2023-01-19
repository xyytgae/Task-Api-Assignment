
from sqlalchemy.orm import Session
from typing import Union
from datetime import date, datetime

from api.schemas import TaskCreate, TaskUpdate
from api.db.entities import TaskEntity
from api.models.status import Status

def create_task(db: Session, task_create: TaskCreate):
    task = TaskEntity(**task_create.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task.to_model()

def get_tasks(db: Session, due_date: Union[str, None], status: Union[Status, None]):
    query = db.query(TaskEntity)
    if due_date and status:
        formatted_due_date = format_due_date(due_date)
        query = query.filter(TaskEntity.due_date == formatted_due_date, TaskEntity.status == status)
    elif due_date:
        formatted_due_date = format_due_date(due_date)
        query = query.filter(TaskEntity.due_date == formatted_due_date)
    elif status:
        query = query.filter(TaskEntity.status == status)
    return [task.to_model() for task in query.all()]

def format_due_date(due_date: str):
    datetime_formatted = datetime.strptime(due_date, "%Y-%m-%d")
    return date(datetime_formatted.year, datetime_formatted.month, datetime_formatted.day)

def update_task(db: Session, id: int, task_update: TaskUpdate):
    task = db.query(TaskEntity).filter(TaskEntity.id == id).first()
    db_task = TaskEntity(**task_update.dict())
    task.title = db_task.title
    task.status = db_task.status
    task.due_date = db_task.due_date
    db.commit()
    db.refresh(task)
    return task.to_model()