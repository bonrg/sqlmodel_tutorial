from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    Depends,
    status
)
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
