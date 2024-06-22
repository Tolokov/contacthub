from fastapi import FastAPI

from app.api.router import router as api_router
from app.config.config import settings

app = FastAPI(
    title=settings.title,
    debug=settings.debug,
    root_path=settings.rootPath
)

app.include_router(api_router, prefix='/api')
