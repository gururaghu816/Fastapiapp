from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import company, job, auth, chat, rag
from database import Base, engine
from models import job as job_model, company as company_model, users as user_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(company.router)
app.include_router(job.router)
app.include_router(chat.router)
app.include_router(rag.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def read_about():
    return {"about": "This is about page"}


@app.get("/contact")
def read_contact():
    return {"contact": "This is contact page"}