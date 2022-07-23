from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    Depends,
    HTTPException

)
from sqlmodel import select
from ..database import get_session
from .. import models


class HeroService:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def create(self, hero: models.HeroCreate) -> models.Hero:
        db_hero = models.Hero.from_orm(hero)
        self.session.add(db_hero)
        await self.session.commit()
        await self.session.refresh(db_hero)
        return db_hero

    async def get_heroes(self, offset: int = 0, limit: int = 100) -> list[models.Hero]:
        heroes = await self.session.execute(
            select(models.Hero).offset(offset).limit(limit)
        )
        heroes = heroes.scalars().all()
        return heroes

    async def get(self, hero_id: int) -> models.Hero:
        hero = await self.session.get(models.Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero

    async def update(self, hero_id: int, hero: models.HeroUpdate) -> models.Hero:
        db_hero = await self.get(hero_id=hero_id)
        hero_data = hero.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        self.session.add(db_hero)
        await self.session.commit()
        await self.session.refresh(db_hero)
        return db_hero

    async def delete(self, hero_id: int) -> dict:
        hero = await self.get(hero_id=hero_id)
        await self.session.delete(hero)
        await self.session.commit()
        return {'ok': True}
