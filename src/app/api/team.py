from fastapi import (
    APIRouter,
    Depends,
    status as st,
    Query
)
from .. import models
from ..services.team import TeamService


router = APIRouter(
    prefix='/teams',
    tags=['Teams'],
)


@router.post("/", response_model=models.TeamRead, status_code=st.HTTP_201_CREATED)
async def create_team(team: models.TeamCreate, service: TeamService = Depends()):
    return service.create(team=team)


@router.get("/", response_model=list[models.TeamRead])
async def get_teams(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        service: TeamService = Depends()):
    return service.get_teams(offset=offset, limit=limit)


@router.get("/{team_id}", response_model=models.TeamRead)
async def get(team_id: int, service: TeamService = Depends()):
    return service.get(team_id=team_id)


@router.patch("/{team_id}", response_model=models.TeamRead)
async def update(team_id: int, team: models.TeamUpdate, service: TeamService = Depends()):
    return service.update(team_id=team_id, team=team)


@router.delete("/{team_id}")
async def delete(team_id: int, service: TeamService = Depends()):
    return service.delete(team_id=team_id)
