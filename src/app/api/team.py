from fastapi import (
    APIRouter,
    Depends,
    status as st,
)
from .. import models
from ..services.team import TeamService


router = APIRouter(
    prefix='/teams',
    tags=['Teams'],
)


@router.post("/", response_model=models.TeamRead, status_code=st.HTTP_201_CREATED)
async def create_hero(team: models.TeamCreate, service: TeamService = Depends()):
    return service.create(team=team)