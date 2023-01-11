"""Define routers of Project."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.db.database import get_db
from api.db.task_datasource import get_task

router = APIRouter()


@router.get('/tasks/{id}')
def get_contexts(id: int, db: Session = Depends(get_db),):
    """Get contexts."""
    return get_task(db=db, id=id)
