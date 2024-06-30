from fastapi import APIRouter, HTTPException, Depends, UploadFile, Request, Form, File, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from bson import ObjectId
from jose import jwt, JWTError
from jwt_handler import signJWT, decodeJWT
from jwt_bearer import JWTBearer
import logging
import os
import shutil
from schema.schemas import list_serial
from datetime import datetime, timedelta
from routes.auth import get_password_hash, verify_password, create_access_token,get_current_user
from models.user import Signup, EmailCheck, OtpCheck, PasswordChange, Token,Login,updateProfile
from config.database import collection_name, fogotPassword
from get_userId import get_current_user_id
from werkzeug.security import generate_password_hash, check_password_hash
# from schema.schemas import fogotserie
import requests
from otp import email_alert

router = APIRouter()
logger = logging.getLogger(__name__)

class Process:
    env = {
        "COOKIE_EXPIRES_TIME": os.getenv("COOKIE_EXPIRES_TIME", "1"),
        "SECRET_KEY": os.getenv("SECRET_KEY", "dc3cc26aa8816c0aa4cb3dbd1c93192b70d324cba8d584a90148bb77658d36daf1c84e128ae5aee5a38df03a489e893b952c90c5c7dc14ceae0a591b289aa2973200e60dba945724bd2394e976c1235e121f622fd2cd32d35b1bcfc69a9c56637e579f4492a985993f38f854a4b391123b18e0cd064c997eceb79fbd2a46ed72869001364f67604c3770101406e6e327a05ba9950277a8654e820c38b163f95f38f6f2e2655326a436dab7f2fab37e755f2df219e48d6f16b7067dbbc1ac4994b2b9e9474fa223706539b97e5871eea210a0812d8cfa48eab46a139eb3d3c3e767742a406ee0b5c12b5faed988610a980b5fc644726583b7143e52af628d874b"),
        "JWT_ALGORITHM": os.getenv("JWT_ALGORITHM", "HS256"),
        "NODE_ENV": os.getenv("NODE_ENV", "production")
    }

def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, Process.env["SECRET_KEY"], algorithms=[Process.env["JWT_ALGORITHM"]])
        user_id: str = payload.get("sub")
        print(user_id)
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        user = collection_name.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        user["_id"] = str(user["_id"])
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# def get_current_user(request: Request):
#     token = request.cookies.get("token")
#     if not token:
#         raise HTTPException(status_code=401, detail="Not authenticated")

#     # Check if the token matches the token saved in MongoDB
#     user = get_user_from_token(token)
#     if user.get("token") != token:
#         raise HTTPException(status_code=401, detail="Invalid token")
    
#     return user

def convert_datetime_to_string(data):
    if isinstance(data, dict):
        return {key: convert_datetime_to_string(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_datetime_to_string(item) for item in data]
    elif isinstance(data, datetime):
        return data.isoformat()
    else:
        return data

# Update login endpoint to generate and return a unique token

from bson import ObjectId

@router.post("/login")
async def login_for_access_token(login: Login):
    user = collection_name.find_one({"name": login.name})
    if not user or not check_password_hash(user["password"], login.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Convert ObjectId to string
    user_id = str(user["_id"])

    # Generate a unique token for the user
    token = signJWT(user_id)
    
    # Return the token in the response
    return token


# Fetch user details endpoint
from bson import ObjectId

@router.get("/userDetails")
async def get_user_details(current_user: str = Depends(get_current_user_id)):
    logger.info("Fetching user details for: %s", current_user)
    user = collection_name.find_one({"_id": ObjectId(current_user)})
    # Convert ObjectId to string
    user["_id"] = str(user["_id"])
    print("adghuk", user)
    return user


# @router.post("/updateProfile")
# async def update_profile(
#    data:updateProfile,current_user: str = Depends(get_current_user_id),
   
# ):
#     update_data = {
#         "name":data.name,
#         "bio": data.bio,
#         "address":data.address,
#         "phoneNumber":data.phoneNumber,
#         "dob": data.dob,
    
#     }

#     if data.avatar:
#         avatar_path = f"avatars/{current_user['_id']}_{data.avatar.filename}"
#         with open(avatar_path, "wb") as buffer:
#             shutil.copyfileobj(data.avatar.file, buffer)
#         update_data["avatar"] = avatar_path

#     collection_name.update_one({"_id": ObjectId(current_user)}, {"$set": update_data})
#     return {"message": "Profile updated successfully"}
@router.post("/updateProfile")
async def update_profile(
    name: str = Form(...),
    bio: str = Form(...),
    address: str = Form(...),
    phoneNumber: str = Form(...),
    dob: str = Form(...),
    profession: str = Form(...),
    avatar: UploadFile = File(None),
    current_user: str = Depends(get_current_user_id),
):
    update_data = {
        "name": name,
        "bio": bio,
        "address": address,
        "phoneNumber": phoneNumber,
        "dob": dob,
        "profession":profession,
    }

    if avatar:
        # Ensure the avatars directory exists
        avatar_dir = "avatars"
        if not os.path.exists(avatar_dir):
            os.makedirs(avatar_dir)
        
        # Save the avatar file
        avatar_path = f"{avatar_dir}/{current_user}_{avatar.filename}"
        with open(avatar_path, "wb") as buffer:
            shutil.copyfileobj(avatar.file, buffer)
        update_data["avatar"] = avatar_path

    # Assuming collection_name is your MongoDB collection
    collection_name.update_one({"_id": ObjectId(current_user)}, {"$set": update_data})
    return {"message": "Profile updated successfully"}

@router.post("/logout")
async def logout():
    response = JSONResponse(content={"message": "Logout successful"}, status_code=200)
    response.delete_cookie("token")
    return response



@router.post("/signup")
async def signup(user: Signup):
    userdetail = list(collection_name.find({"email": user.email}))
    if not userdetail:
        hashed_password = generate_password_hash(user.password)
        user_dict = dict(user)
        user_dict["password"] = hashed_password
        collection_name.insert_one(user_dict)
        return {"message": "Success"}
    else:
        return {"message": "User already exists"}

@router.post("/emailCheck", response_model=bool)
async def check_email_existence(emailcheck: EmailCheck):
    email = emailcheck.email
    user = collection_name.find_one({"email": email})
    if user:
        email_alert("OTP Verification", email)
        return True
    else:
        return False

@router.post("/otpCheck", response_model=bool)
async def otpCheck(details: OtpCheck):
    email = details.email
    otp = details.otp
    user = fogotPassword.find_one({"email": email})
    if user:
        stored_otp = user.get("otp")
        if stored_otp == otp:
            return True
        return False
    return False

@router.post("/passwordChange")
async def change_password(password_change_data: PasswordChange):
    # try:
        email = password_change_data.email
        # old_password = password_change_data.old_password
        newPassword = password_change_data.new_password

        # 1. Find the user by email
        user = collection_name.find_one({"email": email})
        if not user:
            return JSONResponse(status_code=404, content={"message": "User not found."})

        # # 2. Verify the old password
        # if not check_password_hash(user["password"], old_password):
        #     return JSONResponse(status_code=401, content={"message": "Incorrect old password."})

        # 3. Update the user's password in the database
        update_result = collection_name.update_one(
            {"_id": user["_id"]},
            {"$set": {"password": generate_password_hash(newPassword)}}  # Update the password field
        )

        if update_result.modified_count == 1:
            return JSONResponse(status_code=200, content={"message": "Password updated successfully."})
        else:
            return JSONResponse(status_code=500, content={"message": "Failed to update password."})

    # except Exception as e:
    #     print(f"Error during password change: {e}")
    #     return JSONResponse(status_code=500, content={"message": "An error occurred during password change."})