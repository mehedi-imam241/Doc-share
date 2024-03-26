from typing import Optional

from schemas.Response.User import User
from schemas.Response.Response import Response


class UserLoginResponse(Response):
    token: Optional[str] = None
    user: Optional[User] = None

    class Config:
        from_attributes = True