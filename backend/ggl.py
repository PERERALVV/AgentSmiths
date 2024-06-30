from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

# Replace these with your actual Google OAuth client ID and secret
GOOGLE_CLIENT_ID = "300007322715-emkj8lhij77lhg7murj60evpeo4682pl.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:8000/google/callback"

@app.get("/google/login")
async def google_login():
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=email%20profile"
    )
    return RedirectResponse(auth_url)

@app.get("/google/callback")
async def google_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return {"error": "Authorization code not found"}

    token_data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }

    token_response = requests.post("https://oauth2.googleapis.com/token", data=token_data)
    if token_response.status_code != 200:
        return {"error": "Failed to retrieve token from Google", "details": token_response.json()}
    
    token_response_data = token_response.json()
    access_token = token_response_data.get("access_token")

    user_info_response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    if user_info_response.status_code != 200:
        return {"error": "Failed to retrieve user info from Google", "details": user_info_response.json()}
    
    user_info = user_info_response.json()
    return user_info
