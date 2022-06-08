import os, sys
from fastapi import FastAPI
from dotenv import load_dotenv

from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from app.domain.models import User as ModelUser
from app.domain.usecases import User as SchemaUser


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get('/hello-world')
def hello_world():
    return {'hello': 'world'}


@app.post('/user/', response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        name=user.name,
        last_name=user.last_name,
        email=user.email
    )

    db.session.add(db_user)
    db.session.commit()
    return db_user
    