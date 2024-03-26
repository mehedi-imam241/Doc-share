from typing import Optional

from pydantic import BaseModel, EmailStr


class SharedDocBase(BaseModel):
    doc_id: int
    user_mail: EmailStr
    edit_access: Optional[bool] = False
