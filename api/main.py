"""Main."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.task_router import router as task_router

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(task_router, prefix="/api")
