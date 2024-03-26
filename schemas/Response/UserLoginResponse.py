from typing import Optional

from schemas.Response.User import User
from schemas.Response.Response import Response


class UserLoginResponse(Response):
    token: Optional[str] = None
    user: Optional[User] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "token": "Some JWT Token",
                    "user": {
                        "id": 1,
                        "email": "mehedi@gmail.com"
                    }
                }
            ]
        }
    }
