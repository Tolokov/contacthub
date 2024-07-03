import uvicorn

from app.config.setting import settings

if __name__ == '__main__':
    uvicorn.run(
        app='app.main:app',
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
