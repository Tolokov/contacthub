from fastapi import APIRouter

from app.api.v1.logging.router import router as logging_router

from app.api.v1.status.router import router as status_checker_router

from app.api.v1.public.router import router as profiles_router

from app.api.v1.protect.router import router as protect_router

router = APIRouter()

router.include_router(logging_router)
router.include_router(status_checker_router)
router.include_router(profiles_router)
router.include_router(protect_router)
