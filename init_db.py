"""Init Dev DB."""
import logging
import os

from datetime import date

from api.db.entities import Base
from api.db.database import SQLALCHEMY_DATABASE_URL
from api.db.task_datasource import create_task_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def init() -> None:
    """init."""
    with SessionLocal() as db:
        due_date = date(2022, 8, 10)
        create_task_db(db=db, title='sample_task', content='sample_task_content', due_date=due_date, status='Open')


def main() -> None:
    """main."""
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
