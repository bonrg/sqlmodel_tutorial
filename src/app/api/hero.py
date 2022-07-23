from fastapi import (
    APIRouter,
    Depends,
    status as st,
    Query
)
from .. import models
from ..services.hero import HeroService


router = APIRouter(
    prefix='/heroes',
    tags=['Heroes'],
)


@router.post("/", response_model=models.HeroRead, status_code=st.HTTP_201_CREATED)
async def create_hero(hero: models.HeroCreate, service: HeroService = Depends()):
    return await service.create(hero=hero)


@router.get("/", response_model=list[models.HeroRead])
async def get_heroes(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        service: HeroService = Depends()):
    return await service.get_heroes(offset=offset, limit=limit)


@router.get("/{hero_id}", response_model=models.HeroReadWithTeam)
async def get(hero_id: int, service: HeroService = Depends()):
    return await service.get(hero_id=hero_id)


@router.patch("/{hero_id}", response_model=models.HeroRead)
async def update(hero_id: int, hero: models.HeroUpdate, service: HeroService = Depends()):
    return await service.update(hero_id=hero_id, hero=hero)


@router.delete("/{hero_id}")
async def delete(hero_id: int, service: HeroService = Depends()):
    return await service.delete(hero_id=hero_id)
