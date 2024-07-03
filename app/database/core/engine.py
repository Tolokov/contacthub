from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config.setting import settings

from app.database.models.logs import Logs
from app.database.models.token import Token
from app.database.models.resource import Resource
from app.database.models.profile.profile import Profile
from app.database.models.profile.city import City, District

engine = create_async_engine(url=settings.db_url)

session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession,
    expire_on_commit=False, autoflush=True, autocommit=False
)

TABLES = (
    Logs,
    Resource,
    Profile,
    Token,
    District
)


async def create_tables():
    # https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#synopsis-core
    async with engine.begin() as conn:
        for table in TABLES:
            await conn.run_sync(table.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        for table in TABLES:
            await conn.run_sync(table.metadata.drop_all)


async def session() -> AsyncSession:
    async with session_maker() as async_session:
        yield async_session
