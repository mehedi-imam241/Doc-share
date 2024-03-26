from schemas.common.UserBase import UserBase
from pydantic import validator
import re


class UserCreate(UserBase):
    password: str

    @validator('password')
    def validate_password(cls, password):
        if len(password) < 6:
            raise ValueError('Password must be at least 6 characters long')
        if not re.search('[A-Z]', password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search('[a-z]', password):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search('[0-9]', password):
            raise ValueError('Password must contain at least one digit')
        return password

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
