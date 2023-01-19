"""Task."""

from datetime import date
from pydantic import BaseModel
from api.models.status  import Status

class TaskBase(BaseModel):
    title: str
    due_date: date

class TaskCreate(TaskBase):
    content: str

class TaskCreateResponse(TaskCreate):
    id: int
    status: Status

    class Config:
        orm_mode = True

class TaskUpdate(TaskBase):
    status: Status

class TaskUpdateResponse(TaskUpdate):
    id: int
    content: str
    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    content: str
    status: Status
