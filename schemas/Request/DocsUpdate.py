from typing import Optional

from schemas.common.DocsBase import DocsBase


class DocsUpdate(DocsBase):
    title: Optional[str] = None
    description: Optional[str] = None

    # class Config:
    #     from_attributes = True

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "My Updated Doc Title",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
                }
            ]
        }
    }

