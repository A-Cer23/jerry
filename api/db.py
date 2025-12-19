import uuid
import datetime

from sqlmodel import Field, SQLModel, create_engine, Session
from fastapi import Depends
from typing import Annotated

from config import settings

class Request(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

db_url = settings.get_db_url()
engine = create_engine(db_url, pool_size=10, max_overflow=0, echo_pool=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]