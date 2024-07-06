import time
import jwt
from typing import Dict
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

EXPIRY_TIME = 600
Refesh_EXPIRY_TIME = 1800

CURRUENT_USER = ""


def token_response(token: str, refresh_token: str,role: str):
    return {"access_token": token, "refresh_token": refresh_token,"role": role}


# # function used for signing the JWT string
# def signJWT(user_id: str) -> Dict[str, str]:
#     payload = {
#         "user_id": user_id,
#         "expires": time.time() + EXPIRY_TIME,
#         "refresh_expires": time.time() + Refesh_EXPIRY_TIME,
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#     refresh_token = jwt.encode(
#         {"user_id": user_id, "expires": time.time() + Refesh_EXPIRY_TIME},
#         JWT_SECRET,
#         algorithm=JWT_ALGORITHM,
#     )
#     return token_response(token, refresh_token)
def signJWT(user_id: str, role: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + EXPIRY_TIME,
        "refresh_expires": time.time() + Refesh_EXPIRY_TIME,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    refresh_token = jwt.encode(
        {"user_id": user_id, "role": role, "expires": time.time() + Refesh_EXPIRY_TIME},
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )
    return token_response(token, refresh_token,role)

# def decodeJWT(token: str) -> dict:
#     try:
#         decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
#         expires = decoded_token.get("expires", 0)
#         refresh_expires = decoded_token.get("refresh_expires", 0)
#         CURRUENT_USER = decoded_token.get("user_id", 0)

#         if expires >= time.time():
#             return decoded_token
#         elif refresh_expires >= time.time():
#             user_id = decoded_token.get("user_id", None)
#             if user_id:
#                 refreshed_tokens = signJWT(user_id)
#                 return refreshed_tokens
#         return None, None

#     except jwt.ExpiredSignatureError:
#         return None, None
#     except jwt.PyJWTError:
#         return None, None
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        expires = decoded_token.get("expires", 0)
        refresh_expires = decoded_token.get("refresh_expires", 0)

        if expires >= time.time():
            return decoded_token
        elif refresh_expires >= time.time():
            user_id = decoded_token.get("user_id", None)
            role = decoded_token.get("role", None)
            if user_id and role:
                refreshed_tokens = signJWT(user_id, role)
                return refreshed_tokens

        return {"error": "Token expired or invalid"}

    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}