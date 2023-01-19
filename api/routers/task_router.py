"""Define routers of Project."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Union

from api.db.database import get_db
from api.db.task_datasource import get_task
from api.crud.task import create_task, get_tasks, update_task
from api import schemas
from api.models.status import Status

router = APIRouter()


@router.get('/tasks/{id}')
def get_contexts(id: int, db: Session = Depends(get_db),):
    """Get contexts."""
    return get_task(db=db, id=id)

@router.post('/tasks', response_model=schemas.TaskCreateResponse)
def create_contexts(task_body: schemas.TaskCreate, db: Session = Depends(get_db),):
    """Create contexts."""
    return create_task(db, task_body)

@router.get('/tasks', response_model=List[schemas.Task])
def get_contexts(due_date: Union[str, None] = None, status: Union[Status, None] = None, db: Session = Depends(get_db),):
    """Get contexts."""
    return get_tasks(db, due_date, status)

@router.put('/tasks/{id}', response_model=schemas.TaskUpdateResponse)
def update_contexts(id: int, task_body: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """Update contexts."""
    return update_task(db, id, task_body)