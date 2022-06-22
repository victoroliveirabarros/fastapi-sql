from fastapi_sqlalchemy import db

from app.domain.usecases import Usecase
from app.infra.database.repositories.user_repository import UserRepository
from app.services.usecases import CreateUser


def create_user_factory() -> Usecase:
    return CreateUser(
        user_repository=UserRepository(db)
    )