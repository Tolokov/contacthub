from fastapi import APIRouter

from app.api.v1.logging.endpoints.logging import router as logging_router

router = APIRouter()

router.include_router(logging_router, prefix="/logging", tags=["logging"])
