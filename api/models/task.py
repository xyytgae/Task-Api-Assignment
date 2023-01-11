"""Task."""

from datetime import date
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    content: str
    due_date: date
    status: str
