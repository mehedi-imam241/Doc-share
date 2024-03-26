from typing import Optional

from schemas.common.DocsBase import DocsBase


class DocsUpdate(DocsBase):
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True
