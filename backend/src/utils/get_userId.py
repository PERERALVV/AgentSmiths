from utils.jwt_handler import signJWT, decodeJWT
from utils.jwt_bearer import JWTBearer
from fastapi.exceptions import HTTPException
from fastapi import Depends

def get_current_user_id(token: str = Depends(JWTBearer())):
    try:
        payload = decodeJWT(token)
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid user ID in token")
        return user_id
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")