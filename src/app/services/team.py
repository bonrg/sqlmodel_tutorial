from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    Depends,
    HTTPException
)
from sqlmodel import select
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

    async def get_teams(self, offset: int = 0, limit: int = 100) -> list[models.Team]:
        teams = await self.session.execute(
            select(models.Team).offset(offset).limit(limit)
        )
        teams = teams.scalars().all()
        return teams
    
    async def get(self, team_id: int) -> models.Team:
        team = await self.session.get(models.Team, team_id)
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        return team

    async def update(self, team_id: int, team: models.TeamUpdate) -> models.Team:
        db_team = await self.get(team_id=team_id)
        team_data = team.dict(exclude_unset=True)
        for key, value in team_data.items():
            setattr(db_team, key, value)
        self.session.add(db_team)
        await self.session.commit()
        await self.session.refresh(db_team)
        return db_team

    async def delete(self, team_id: int) -> dict:
        team = await self.get(team_id=team_id)
        await self.session.delete(team)
        await self.session.commit()
        return {'ok': True}
