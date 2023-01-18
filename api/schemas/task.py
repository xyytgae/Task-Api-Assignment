"""Task."""

from datetime import date
from pydantic import BaseModel, Field
from api.models.status  import Status

class TaskBase(BaseModel):
    title: str
    content: str
    due_date: date

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int
    status: Status

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    status: Status
