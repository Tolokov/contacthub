from fastapi import APIRouter

from app.api.v1.status.endpoints.status_checker import router as status_checker_router

router = APIRouter()

router.include_router(status_checker_router, prefix='/status', tags=['status'])
