from pydantic import BaseModel


class Unauthorized(BaseModel):
    error: str = 'Unauthorized'


class InternalServerError(BaseModel):
    error: str = 'Internal Server Error'


class HandledError(BaseModel):
    error: str
    