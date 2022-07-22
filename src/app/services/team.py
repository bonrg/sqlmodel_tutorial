from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    Depends,
    status
)
from ..database import get_session
from .. import models


class TeamService:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def create(self, team: models.TeamCreate) -> models.Team:
        db_team = models.Team.from_orm(team)
        self.session.add(db_team)
        await self.session.commit()
        await self.session.refresh(db_team)
        return db_team
