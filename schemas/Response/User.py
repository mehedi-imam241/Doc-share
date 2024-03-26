from schemas.Response.Docs import Docs
from schemas.Response.Response import Response
from schemas.common.UserBase import UserBase


class User(UserBase,Response):
    id:  int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "email": "mehedi@gmail.com",
                    "success": True,
                    "message": "Request Successful"
                }
            ]
        }
    }
