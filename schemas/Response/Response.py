from pydantic import BaseModel

class Response(BaseModel):
    success: bool = True
    message: str = "Request Successful"

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "success": True,
                    "message": "Request Successful"
                }
            ]
        }
    }