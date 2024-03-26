from pydantic import BaseModel


class UserLoginPayload(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True