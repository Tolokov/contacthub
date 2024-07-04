from sqlalchemy import insert

from sqlalchemy.sql.sqltypes import Enum, String, DateTime, Integer, String, Boolean, JSON

from app.database.models.logs import LoggerLevel, ClientLevel


async def fill_database_testing_datas(table, conn):
    data = {}
    for name, col in table.__table__.columns.items():
        if '_id' in name:
            data[name] = 1
        elif name == 'id':
            continue
        elif isinstance(col.type, Enum):
            if col.type == LoggerLevel.title:
                data[name] = dir(LoggerLevel)[1]
            elif col.type == ClientLevel.title:
                data[name] = dir(ClientLevel)[1]
        elif isinstance(col.type, String):
            data[name] = 'TEST-' + str(col.type)
        elif isinstance(col.type, Integer):
            import random
            data[name] = random.randint(0, 1000)
        elif isinstance(col.type, JSON):
            data[name] = {'title': 'title', 'data': 'data'}

    await conn.execute(insert(table).values(data))
    data.clear()
