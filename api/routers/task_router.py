"""Define routers of Project."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.db.database import get_db
from api.db.task_datasource import get_task
from api.crud.task import create_task
from api import schemas

router = APIRouter()


@router.get('/tasks/{id}')
def get_contexts(id: int, db: Session = Depends(get_db),):
    """Get contexts."""
    return get_task(db=db, id=id)

@router.post('/tasks', response_model=schemas.TaskCreateResponse)
async def create_contexts(task_body: schemas.TaskCreate, db: Session = Depends(get_db),):
    """Create contexts."""
    return await create_task(db, task_body)
