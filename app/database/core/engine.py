from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config.setting import settings

from app.database.models import logs, token, resource
from app.database.models.profile import city, profile, raw_profile

from app.lib.tests import fill_database_testing_datas

engine = create_async_engine(url=settings.db_url)

session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession,
    expire_on_commit=False, autoflush=True, autocommit=False
)

TABLES = (
    logs.Logs,
    resource.Resource,
    token.Token,

    city.District, city.City,
    profile.Profile, profile.Contact, profile.Sector, profile.Text,

    raw_profile.Raw
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


async def fill_tables(count_testing_rows=10):
    async with engine.begin() as conn:
        for table in TABLES:
            for i in range(count_testing_rows):
                await fill_database_testing_datas(table, conn)


async def session() -> AsyncSession:
    async with session_maker() as async_session:
        yield async_session
