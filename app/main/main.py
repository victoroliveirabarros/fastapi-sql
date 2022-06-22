import os, sys
from http import HTTPStatus
from fastapi import FastAPI
from fastapi import Response
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv

from app.main.adapters import fast_api_adapter
from app.domain.usecases import CreateUserParams, CreateUserResponse
from app.main.factories import create_user_factory
from app.main.routes.helpers import HandledError


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

ROUTES_TAGS = ['User']


@app.get('/hello-world')
def hello_world():
    return {'hello': 'world'}


@app.post(
    '/user',
    responses={
        HTTPStatus.CREATED.value: {
            'model': CreateUserResponse
        },
        HTTPStatus.BAD_REQUEST.value: {
            'model': HandledError, 'description': 'Company or tenant not found'
        }
    },
    status_code=HTTPStatus.CREATED,
    tags=ROUTES_TAGS
)
def create_user(body: CreateUserParams, response: Response):
    request = {'body': body, 'headers': None, 'query': None}
    result = fast_api_adapter(request, create_user_factory()) 
    response.status_code = result.status_code
    return result.body
    