from schemas.common.DocsBase import DocsBase


class DocsCreate(DocsBase):
    pass

    model_config = {
         "json_schema_extra": {
            "examples": [
                {
                    "title": "My Doc Title",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
                }
            ]
        }
    }
