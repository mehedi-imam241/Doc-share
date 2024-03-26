from pydantic import BaseModel


class DocsBase(BaseModel):
    title: str
    description: str



