from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import AsyncAdaptedQueuePool

from app.config import settings


metadata = MetaData()
Base = declarative_base(metadata=metadata)

engine = create_async_engine(
    settings.DATABASE_URL,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=200,
    max_overflow=100,
    pool_timeout=300,
)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
