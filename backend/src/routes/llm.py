from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import google.generativeai as genai

import os

from dotenv import load_dotenv
load_dotenv()
google_api_key = os.environ.get("google_api_key")
groq_api_key=os.environ.get("groq_api_key")

def gemini(temp=0.1):
    return ChatGoogleGenerativeAI(model="gemini-pro", client="google", google_api_key= google_api_key , temperature=temp) #init the model
def gemini_chat(temp=0.7):
    return ChatGoogleGenerativeAI(model="gemini-pro", client="google", google_api_key= google_api_key , temperature=temp , convert_system_message_to_human=True) #init the model
def gemini_embeddings():
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001",task_type="retrieval_query",google_api_key=google_api_key)

def groq_chat(temp=0):
    return ChatGroq(temperature=temp, groq_api_key=groq_api_key ,model_name="mixtral-8x7b-32768")

class Ggemini:
    def __init__(self):
        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
    def chatGemini(self, msg):
        response = self.chat.send_message(msg)
        return response.text
    def gethistory(self):
        return self.chat.history
    def getGeminiResponse(self, msg):
        response = self.model.generate_content(msg)
        return response.text
