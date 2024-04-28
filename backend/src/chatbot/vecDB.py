import os
import sys
from langchain_community.vectorstores import Chroma
from llm import *
from rag import *
if __name__ == "__main__":
    splits=get_semantic_splits()
    vectorstore = Chroma.from_documents(documents=splits, embedding=gemini_embeddings(), persist_directory="./chroma_db")
    vectorstore.persist()
    print("vectorstore created")
    

def getDB():
    db_directory = "./chroma_db"
    if not os.path.exists(db_directory):
        splits = get_semantic_splits()
        vectorstore = Chroma.from_documents(documents=splits, embedding=gemini_embeddings(), persist_directory=db_directory)
        vectorstore.persist()
        print("vectorstore created")

    vectorstore_disk = Chroma(
                        persist_directory=db_directory,       # Directory of db
                        embedding_function=gemini_embeddings()   # Embedding model
                   )
    return vectorstore_disk

def initDB():
    db_directory = "./chroma_db"
    if not os.path.exists(db_directory):
        splits = get_semantic_splits()
        vectorstore = Chroma.from_documents(documents=splits, embedding=gemini_embeddings(), persist_directory=db_directory)
        vectorstore.persist()
        print("vectorstore created")
    else:
        print("vectorstore already exists")