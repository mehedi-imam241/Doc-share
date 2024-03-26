from typing import Optional

from pydantic import BaseModel


class SharedDocBase(BaseModel):
    doc_id: int
    user_mail: str
    edit_access: Optional[bool] = False
