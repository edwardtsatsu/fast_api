from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str


class UserIn(BaseModel):
    id: int
    username: str
    email: str


class UserOut(BaseModel):
    name: str
