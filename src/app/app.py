from fastapi import FastAPI
from . import api
from .database import init_db

tags_metadata = [
    {
        'name': 'Heroes',
        'description': 'Heroes',
    },
    {
        'name': 'Teams',
        'description': 'Teams',
    },
]

app = FastAPI(
    title='SqlModel Tutorial',
    description='SqlModel Tutorial',
    version='1.0.0',
    openapi_tags=tags_metadata,
)


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(api.router)
