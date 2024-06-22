from fastapi import APIRouter

from app.api.status.status_checker import router as status_checker_router

router = APIRouter()

router.include_router(status_checker_router, prefix='/v1', tags=['status'])
