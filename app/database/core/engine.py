from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config.config import settings

from app.database.models.logs import Logs
from app.database.models.token import Token
from app.database.models.resource import Resource
from app.database.models.addition import Addition
from app.database.models.profile.profile import Profile


engine = create_async_engine(url=settings.db_url)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False, echo=True)


async def create_tables():
    # https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#synopsis-core
    async with engine.begin() as conn:
        await conn.run_sync(Logs.metadata.create_all)
        await conn.run_sync(Token.metadata.create_all)
        await conn.run_sync(Resource.metadata.create_all)
        await conn.run_sync(Addition.metadata.create_all)
        # await conn.run_sync(Profile.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Logs.metadata.drop_all)
        await conn.run_sync(Token.metadata.drop_all)
        await conn.run_sync(Resource.metadata.drop_all)
        await conn.run_sync(Addition.metadata.drop_all)
        # await conn.run_sync(Profile.metadata.drop_all)


async def async_engine_connect_functions():
    async with engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))
        print(f"{res=}")
