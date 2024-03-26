from schemas.common.DocsBase import DocsBase
from schemas.Response.Response import Response


class Docs(DocsBase, Response):
    owner_id: int
    id: int

    class Config:
        from_attributes = True
