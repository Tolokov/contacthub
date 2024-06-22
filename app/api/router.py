from fastapi import APIRouter

from app.api.service.logging import router as logging_router
from app.api.service.status_checker import router as status_checker_router


router = APIRouter()

router.include_router(logging_router, prefix='/v1', tags=['status'])
router.include_router(status_checker_router, prefix='/v1', tags=['status'])
