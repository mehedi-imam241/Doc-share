from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from utils.JWT_util import verifyJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = verifyJWT(token)
    if user is None:
        raise Exception('Unauthorized')
    return user
