from db import create_db_and_tables, SessionDep, Request
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import select, func



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/requests/")
def request(session: SessionDep) -> Request:
    r = Request()
    session.add(r)
    session.commit()
    session.refresh(r)
    return r

@app.get("/requests/")
def requests(session: SessionDep) -> dict:
    statement = select(func.count()).select_from(Request)
    total = session.exec(statement).one()
    return {"total": total}