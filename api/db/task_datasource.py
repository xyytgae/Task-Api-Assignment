"""Task datasource."""
from datetime import date
from sqlalchemy.orm import Session

from api.db.entities import TaskEntity

def create_task_db(db: Session, title: str, content: str, due_date: date, status: str):
    """Create Organization."""
    db_task = TaskEntity(
        title=title,
        content=content,
        due_date=due_date,
        status=status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)


def get_task(db: Session, id: int):
    db_task = db.query(TaskEntity).filter(TaskEntity.id == id).first()
    return db_task.to_model()