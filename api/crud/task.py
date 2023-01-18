
from sqlalchemy.orm import Session
from api.schemas import TaskCreate
from api.db.entities import TaskEntity

async def create_task(db: Session, task_create: TaskCreate):
    task = TaskEntity(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task