from schemas.common.DocsBase import DocsBase
from schemas.Response.Response import Response


class Docs(DocsBase, Response):
    owner_id: int
    id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "My Doc Title",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                    "owner_id": 1,
                    "id": 1
                }
            ]
        }
    }
