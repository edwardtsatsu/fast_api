from pydantic import BaseModel
from sqlalchemy import DateTime


class UserIn(BaseModel):
    username: str
    email: str
    password: str


class UserOut(BaseModel):
    username: str
    email: str
    password: str
    created_on: str
