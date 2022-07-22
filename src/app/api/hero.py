from fastapi import (
    APIRouter,
    Depends,
    status as st,
)
from .. import models
from ..services.hero import HeroService


router = APIRouter(
    prefix='/heroes',
    tags=['Heroes'],
)


@router.post("/", response_model=models.HeroRead, status_code=st.HTTP_201_CREATED)
async def create_hero(hero: models.HeroCreate, service: HeroService = Depends()):
    return service.create(hero=hero)
