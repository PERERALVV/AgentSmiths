from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker

from langchain_community.document_loaders import TextLoader

from llm import *
import os


script_dir = os.path.dirname(os.path.realpath(__file__))
content_path = os.path.join(script_dir, 'content.txt')


def get_splits():
    loader = TextLoader(content_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return splits


# -----------------------------------------------------------------------------------------------------------
def get_semantic_splits():
    loader = TextLoader(content_path)

    docs = loader.load()
    text=[]
    for doc in docs:
        text.append(doc.page_content)

    text_splitter = SemanticChunker(gemini_embeddings())
    splits = text_splitter.create_documents(text)
    return splits





# -----------------------------------------------------------------------------------------------------------



# splits=get_semantic_splits()
# splits=get_splits()
# for split in splits:
#     print(split.page_content)
#     print("-------------------------------------------------------------------------------------------")
#     print("-------------------------------------------------------------------------------------------")
#     print("-------------------------------------------------------------------------------------------")
#     print("-------------------------------------------------------------------------------------------")