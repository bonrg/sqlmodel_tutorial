from fastapi import APIRouter

from . import (
    hero,
    team
)


router = APIRouter()
router.include_router(hero.router)
router.include_router(team.router)
