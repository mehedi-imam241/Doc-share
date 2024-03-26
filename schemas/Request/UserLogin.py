from pydantic import BaseModel


class UserLoginPayload(BaseModel):
    email: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "mehedi@gmail.com",
                    "password": "Password123"

                }
            ]
        }
    }