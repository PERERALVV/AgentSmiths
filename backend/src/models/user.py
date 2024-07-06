from pydantic import BaseModel, EmailStr
from typing import Optional,List
class Signup(BaseModel):
    name: str
    email: EmailStr
    password: str
    # role:str
    
class Login(BaseModel):
    name: str
    password: str
    # role:str
    
class EmailCheck(BaseModel):
    email: EmailStr

class PasswordChange(BaseModel):
    email: EmailStr
    # old_password: str
    new_password: str

# Other models like OtpCheck if needed
class OtpCheck(BaseModel):
    otp: str
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str
    
class updateProfile(BaseModel):
    
    # name:Optional[str] 
    # bio:Optional[str]
    # address:Optional[str]
    # phoneNumber:Optional[str]
    # dob:Optional[str]
    # avatar:Optional[str]
     name: str
     bio: str
     address: str
     phoneNumber: str
     dob: str
     profession: str

class UserModel(BaseModel):
    name: str
    email: str
    role: str
    
class ProjectModel(BaseModel):
    userID: str
    projectName: str

class ChatMessage(BaseModel):
    message: str
    direction: str
    sender: str

class ReviewChat(BaseModel):
    id: Optional[str]
    chat: List[ChatMessage] = []

class UpdateClusterRequest(BaseModel):
    action: str
    cluster_id: str

class RephraseRequest(BaseModel):
    question: str