from fastapi import APIRouter

from app.api.v1.protect.endpoints.protect import router as protect_router

router = APIRouter()

router.include_router(protect_router, prefix="/protect", tags=["protect"])
