from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from models import Company
from db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

