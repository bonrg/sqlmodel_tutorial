from fastapi import FastAPI
from . import api

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

app.include_router(api.router)
