from fastapi import APIRouter

from app.api.v1.public.endpoints.profile import router as profile_router
from app.api.v1.public.endpoints.profiles import router as profiles_router

router = APIRouter()

router.include_router(profile_router, prefix="/profile", tags=["profile"])
router.include_router(profiles_router, prefix="/profiles", tags=["profiles"])
