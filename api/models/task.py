"""Task."""

from datetime import date
from pydantic import BaseModel
from api.models.status import Status

class Task(BaseModel):
    id: int
    title: str
    content: str
    due_date: date
    status: Status
