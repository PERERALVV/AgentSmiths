from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
import base64
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus

load_dotenv()

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):
    topic: str
    message: str
    status: str


SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_FROM = os.getenv("SMTP_EMAIL")
EMAIL_TO = os.getenv("SMTP_EMAIL")

username = quote_plus('ayesha')
password = quote_plus('pTPivwignr4obw2U')
cluster = 'cluster0.mhaksto.mongodb.net'
uri = f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0&ssl=true'
client = AsyncIOMotorClient(uri)
db = client['AGENTSMTHS']
collection = db['feedback']


def extract_base64_images(html):
    img_tags = re.findall(
        r'<img src="data:image/(png|jpeg|jpg);base64,([^"]+)"', html)
    images = []
    for i, img in enumerate(img_tags):
        image_type, image_data = img
        image_data = base64.b64decode(image_data)
        image_filename = f'image{i}.{image_type}'
        images.append((image_filename, image_data, image_type))
        html = html.replace(
            f'data:image/{image_type};base64,{img[1]}', f'cid:{image_filename}')
    return html, images


@app.post("/send-email")
async def send_email(request: EmailRequest):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = request.topic

        html_content, images = extract_base64_images(request.message)

        body = MIMEText(html_content, "html")
        msg.attach(body)

        for filename, image_data, image_type in images:
            image = MIMEImage(image_data, _subtype=image_type)
            image.add_header('Content-ID', f'<{filename}>')
            msg.attach(image)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

        feedback_data = {"topic": request.topic,
                         "message": request.message, "status": request.status}
        result = await collection.insert_one(feedback_data)
        if not result.inserted_id:
            raise HTTPException(
                status_code=500, detail="Failed to save feedback")

        return {"message": "Email sent and feedback saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
