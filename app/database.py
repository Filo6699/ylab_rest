from uuid import UUID

from decouple import config as env
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


PSQL_USER = env("PSQL_USER")
PSQL_PASSWORD = env("PSQL_PASSWORD")
PSQL_HOST = env("PSQL_HOST")
PSQL_PORT = env("PSQL_PORT")
PSQL_DATABASE = env("PSQL_DATABASE")

DATABASE_URL = f"postgresql+asyncpg://{PSQL_USER}:{PSQL_PASSWORD}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DATABASE}"

engine = create_async_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = async_sessionmaker(engine)


def convert_to_UUID(uuid: str) -> UUID:
    try:
        return UUID(uuid)
    except ValueError:
        raise ValueError("Некорректный формат UUID.")


async def get_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
