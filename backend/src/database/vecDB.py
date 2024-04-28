import os

from langchain_community.vectorstores import Chroma
from src.routes.llm import *
from src.utils.rag import Rag
import shutil

# if __name__ == "__main__":
#     retriver = Rag("../const/chatbot_knowledge.txt")
#     splits=retriver.get_semantic_splits()
#     vectorstore = Chroma.from_documents(documents=splits, embedding=gemini_embeddings(), persist_directory="../models/support_chatbot")
#     vectorstore.persist()
#     print("vectorstore created")
    

def getDB():
    db_directory = "src/models/support_chatbot"
    if not os.path.exists(db_directory):
        print("vectorstore corrupted or not initialized")

    vectorstore_disk = Chroma(
                        persist_directory=db_directory,       # Directory of db
                        embedding_function=gemini_embeddings()   # Embedding model
                   )
    return vectorstore_disk


def initDB():
    db_directory = "src/models/support_chatbot"
    retriver = Rag("src/const/chatbot_knowledge.txt")
    # Delete everything in the directory
    if os.path.exists(db_directory):
        shutil.rmtree(db_directory)
    os.makedirs(db_directory)
    # intialize the db
    splits = retriver.get_semantic_splits()
    vectorstore = Chroma.from_documents(documents=splits, embedding=gemini_embeddings(), persist_directory=db_directory)
    vectorstore.persist()
    print("vectorstore created")
