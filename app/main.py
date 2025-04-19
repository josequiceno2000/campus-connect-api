from fastapi import FastAPI
from .database import async_engine
from .models import user, event, participation
import asyncio

app = FastAPI()

async def create_db_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(user.Base.metadata.create_all)
        await conn.run_sync(event.Base.metadata.create_all)
        await conn.run_sync(participation.Base.metadata.create_all)

@app.on_event("startup")
async def startup_event():
    await create_db_tables()