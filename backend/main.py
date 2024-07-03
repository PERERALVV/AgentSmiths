# from fastapi import FastAPI,Request,Depends
# from routes.route import router
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import OAuth2AuthorizationCodeBearer
# import os
# import requests
# from fastapi.responses import RedirectResponse
# # from dotenv import load_dotenv
# # load_dotenv()
# from fastapi.staticfiles import StaticFiles





# app = FastAPI()
# origins=["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["Authorization", "Content-Type"],
# )
# app.mount("/avatars", StaticFiles(directory="avatars"), name="avatars")

# app.include_router(router)
# CLIENT_ID = os.getenv("300007322715-emkj8lhij77lhg7murj60evpeo4682pl.apps.googleusercontent.com")
# CLIENT_SECRET = os.getenv("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")
# REDIRECT_URI = "http://127.0.0.1:8000/google/callback"

# oauth2_scheme = OAuth2AuthorizationCodeBearer(authorizationUrl="https://accounts.google.com/o/oauth2/auth", tokenUrl="https://oauth2.googleapis.com/token")

# @app.get("/google/login")
# def google_login():
#     auth_url = (
#         "https://accounts.google.com/o/oauth2/auth"
#         "?response_type=code"
#         f"&client_id={CLIENT_ID}"
#         f"&redirect_uri={REDIRECT_URI}"
#         "&scope=email%20profile"
#     )
#     return RedirectResponse(auth_url)

# @app.get("/google/callback")
# async def google_callback(request: Request):
#     code = request.query_params.get("code")
#     if not code:
#         return {"error": "Authorization code not found"}

#     token_data = {
#         "code": code,
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#         "redirect_uri": REDIRECT_URI,
#         "grant_type": "authorization_code"
#     }

#     token_response = requests.post("https://oauth2.googleapis.com/token", data=token_data)
#     token_response_data = token_response.json()
#     access_token = token_response_data.get("access_token")

#     user_info_response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
#     user_info = user_info_response.json()

#     # Handle user info (e.g., create or authenticate user in your database)
#     return user_info

from fastapi import FastAPI
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(router)

# # Your OAuth2 configuration
# CLIENT_ID = os.getenv("CLIENT_ID")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# REDIRECT_URI = "http://127.0.0.1:8000/google/callback"

# if not CLIENT_ID or not CLIENT_SECRET:
#     raise EnvironmentError("CLIENT_ID and CLIENT_SECRET must be set in the environment variables")

# @app.get("/google/login")
# def google_login():
#     auth_url = (
#         "https://accounts.google.com/o/oauth2/auth"
#         "?response_type=code"
#         f"&client_id={CLIENT_ID}"
#         f"&redirect_uri={REDIRECT_URI}"
#         "&scope=email%20profile"
#     )
#     return RedirectResponse(auth_url)

# @app.get("/google/callback")
# async def google_callback(request: Request):
#     code = request.query_params.get("code")
#     if not code:
#         return {"error": "Authorization code not found"}

#     token_data = {
#         "code": code,
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#         "redirect_uri": REDIRECT_URI,
#         "grant_type": "authorization_code"
#     }

#     token_response = requests.post("https://oauth2.googleapis.com/token", data=token_data)
#     token_response_data = token_response.json()
#     access_token = token_response_data.get("access_token")

#     user_info_response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
#     user_info = user_info_response.json()

#     # Handle user info (e.g., create or authenticate user in your database)
#     return user_info
