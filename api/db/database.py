"“”Database settings.“”"
from api.db.entities import Base

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, scoped_session, sessionmaker
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=True, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Get DB Session."""
    with SessionLocal() as db:
        yield db
