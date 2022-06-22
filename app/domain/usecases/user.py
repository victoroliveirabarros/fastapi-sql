from abc import abstractmethod
from pydantic import BaseModel

from app.services.helpers.http import HttpResponse
from app.domain.usecases.usecase import Usecase


# class User(BaseModel):
#     id: int
#     name: str
#     last_name: str = None
#     email: str


class CreateUserParams(BaseModel):
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class CreateUserResponse(BaseModel):
    name: str
    last_name: str
    email: str


class CreateUser(Usecase):
    @abstractmethod
    def execute(self, create_user: CreateUserParams) -> HttpResponse:
        raise NotImplementedError()
