import os
from routes.llm import GeminiEmbeddingFunction
from utils.rag import Rag
import shutil
import chromadb
from typing import List

def create_chroma_db(documents:List, path:str, name:str):

    chroma_client = chromadb.PersistentClient(path=path)
    db = chroma_client.create_collection(name=name, embedding_function=GeminiEmbeddingFunction())

    for i, d in enumerate(documents):
        db.add(documents=d, ids=str(i))

    return db, name

def load_chroma_collection(path, name):

    chroma_client = chromadb.PersistentClient(path=path)
    db = chroma_client.get_collection(name=name, embedding_function=GeminiEmbeddingFunction())

    return db

def getDB():
    db_directory = os.path.join(os.environ['ROOT_PATH'], "local databases", "support_chatbot")
    if not os.path.exists(db_directory):
        print("vectorstore corrupted or not initialized")
    db=load_chroma_collection(path=db_directory, name="support_chatbot")
    return db
                              
def initDB():
    db_directory = os.path.join(os.environ['ROOT_PATH'], "local databases", "support_chatbot")
    konwledge_file = os.path.join(os.environ['ROOT_PATH'], "const", "chatbot_knowledge.txt")
    retriver = Rag(konwledge_file)
    # Delete everything in the directory
    if os.path.exists(db_directory):
        shutil.rmtree(db_directory)
    os.makedirs(db_directory)
    # intialize the db
    splits = retriver.get_splits()
    page_contents = [doc.page_content for doc in splits]
    create_chroma_db(documents=page_contents, 
                            path=db_directory,
                            name="support_chatbot")#this will return dbuuid and dbname which is not needed in this case


if __name__ == "__main__":
    initDB()
    pass








