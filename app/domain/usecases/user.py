import imp
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    last_name: str = None
    email: str

    class Config:
        orm_mode = True