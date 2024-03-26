from pydantic import BaseModel

class Response(BaseModel):
    success: bool = True
    message: str = "Request Successful"

    class Config:
        from_attributes = True