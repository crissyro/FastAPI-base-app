import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api import router as api_router
from core.config import settings
from core.models import db_helper
from core.models.base import Base

@asynccontextmanager
async def lifespan(app_: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    #shutdown
    await db_helper.dispose()



app = FastAPI(
    lifespan=lifespan,
)

app.include_router(
    api_router,
    prefix=settings.api_prefix.prefix,
    )

if __name__ == '__main__':
    uvicorn.run(
        "main:app", 
        host=settings.run.host, 
        port=settings.run.port, 
        reload=settings.run.reload
    )