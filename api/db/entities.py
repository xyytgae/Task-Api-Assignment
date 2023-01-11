"""Entifies."""


import os
from datetime import datetime
from functools import lru_cache

from sqlalchemy import TIMESTAMP, DATE, Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from api.models.task import Task


Base = declarative_base()

class TaskEntity(Base):
    """Task Entity."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)
    status = Column(String, nullable=False)
    due_date = Column(DATE, nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())

    def to_model(self) -> Task:
        return Task(
            title=self.title,
            content=self.content,
            due_date=self.due_date,
            status=self.status
        )