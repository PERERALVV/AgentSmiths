from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from chromadb import Documents, EmbeddingFunction, Embeddings
from const.ProjectConst import USE_JSON
import time
import os
from typing import Any, Dict

import importlib
LOG = getattr(importlib.import_module('core.logger'), 'log')

from dotenv import load_dotenv
load_dotenv()
google_api_key = os.environ.get("google_api_key")
google_api_keys = [os.environ.get("google_api_key1"), os.environ.get("google_api_key2"), os.environ.get("google_api_key3"), os.environ.get("google_api_key4"), os.environ.get("google_api_key5")]
groq_api_key=os.environ.get("groq_api_key")


# def groq_chat(temp=0):
#     return ChatGroq(temperature=temp, groq_api_key=groq_api_key ,model_name="mixtral-8x7b-32768")

# def gemini(temp=0.1):
#     return ChatGoogleGenerativeAI(model="gemini-pro", client="google", google_api_key= google_api_key , temperature=temp) #init the model
# def gemini_chat(temp=0.7):
#     return ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", client="google", google_api_key= google_api_key , temperature=temp , convert_system_message_to_human=True) #init the model

def gemini_embeddings():
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001",task_type="retrieval_query",google_api_key=google_api_key)
# latest version of gemini implementation
class Ggemini:
    """A class to interact with the Gemini AI model.

    Attributes:
        generation_config (dict): Configuration for the AI model generation.
        safety_settings (list): List of safety settings for the AI model.
        model (genai.GenerativeModel): The Gemini AI model.
        chat (genai.Chat): The chat session with the AI model.
    """

    def __init__(self, system_instruction: str | None = None, json: bool = False, temp: float = 0.7, tools: Dict[str, Any] | None = None):
        """Initializes the Ggemini class.

        Args:
            system_instruction (str, optional): System instruction for the AI model. Defaults to None.
            json (bool, optional): If True, the response_mime_type in the generation_config is set to "application/json". Defaults to False.
            temp (float, optional): The temperature for the AI model generation. Defaults to 0.7.
            tools (Dict[str, Any], optional): Tools for the AI model. Defaults to None.
        """

        self.tools = tools
        genai.configure(api_key=google_api_key)
        if json:
            self.generation_config = {
                "temperature": temp,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
                "response_mime_type": "application/json",
            }
        else:
            self.generation_config = {
                "temperature": temp,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
            }

        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        if system_instruction == "":
            system_instruction = None

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest",
            safety_settings=self.safety_settings,
            generation_config=self.generation_config,
            system_instruction=system_instruction,
            tools=tools,
        )
        self.chat = self.model.start_chat(history=[])

    def chatGemini(self, msg: str):
        """Sends a message to the AI model and returns its response.

        Args:
            msg (str): The message to send.

        Returns:
            str: The AI model's response.
        """
        for i in range(20):  # maximum of 20 attempts
            try:
                response = self.chat.send_message(msg)
                if response.text is None:
                    raise Exception("Empty response from the model")
                return response.text
            except Exception as e:
                LOG.error(f"Request failed with {e}, retrying in {2**i} seconds...")
                original_chat = self.chat.history
                global google_api_key
                google_api_key = google_api_keys[google_api_keys.index(google_api_key) + 1] if google_api_key in google_api_keys and google_api_keys.index(google_api_key) + 1 < len(google_api_keys) else google_api_keys[0]
                LOG.info(f"Switched to key number{google_api_keys.index(google_api_key)}")
                genai.configure(api_key=google_api_key)
                time.sleep(2**i)  # wait for 2^i seconds before retrying
                self.chat.history=original_chat
        return ""  # return None if all attempts fail


    def getGeminiResponse(self, msg):
        """Generates content from the AI model based on a message.

        Args:
            msg (str): The message to generate content from.

        Returns:
            str: The generated content.
        """


        for i in range(20):  # maximum of 20 attempts
            try:
                response = self.model.generate_content(msg)
                if self.tools is not None:
                    if response.candidates[0].content.parts[0].text is None:
                        raise Exception("Empty response from the model")
                    return response.candidates[0].content.parts[0].text
                if response.text is None:
                    raise Exception("Empty response from the model")
                return response.text
            except Exception as e:
                LOG.error(f"Request failed with {e}, retrying in {2**i} seconds...")
                google_api_key = os.environ.get("google_api_key1")
                google_api_key = google_api_keys[google_api_keys.index(google_api_key) + 1] if google_api_key in google_api_keys and google_api_keys.index(google_api_key) + 1 < len(google_api_keys) else google_api_keys[0]
                genai.configure(api_key=google_api_key)
                LOG.info(f"Switched to key number{google_api_keys.index(google_api_key)}")
                # LOG.error(response) #BUG: DONT USE THIS, local variable 'response' referenced before assignment
                time.sleep(2**i)  # wait for 2^i seconds before retrying
        return ""  # return None if all attempts fail
    
    def gethistory(self):
        """Gets the chat history with the AI model.

        Returns:
            list: The chat history.
        """
        return self.chat.history
    
    def sethistory(self, history):
        """
        Sets the chat history for the current instance.

        Parameters:
        - history: A list or any iterable containing the chat history items.
        """
        self.chat.history = history

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        genai.configure(api_key=google_api_key)
        model = "models/embedding-001"
        title = "Custom query"
        return genai.embed_content(model=model,
                                   content=input,
                                   task_type="retrieval_document",
                                   title=title)["embedding"]





if __name__ == "__main__":
    pass
