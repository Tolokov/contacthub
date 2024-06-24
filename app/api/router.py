from fastapi import APIRouter

from app.api.service.logging import router as logging_router
from app.api.service.status_checker import router as status_checker_router

from app.api.public.profile import router as profile_router
from app.api.public.profiles import router as profiles_router

from app.api.protect.protect import router as protect_router

router = APIRouter()

router.include_router(logging_router, prefix='/v1', tags=['logging'])
router.include_router(status_checker_router, prefix='/v1', tags=['status'])

router.include_router(profile_router, prefix='/v1', tags=['profile'])
router.include_router(profiles_router, prefix='/v1', tags=['profiles'])

router.include_router(protect_router, prefix='/v1', tags=['protect'])
