from schemas.Response.Docs import Docs
from schemas.Response.Response import Response
from schemas.common.UserBase import UserBase


class User(UserBase,Response):
    id:  int
    docs: list[Docs] = []

    class Config:
        from_attributes = True