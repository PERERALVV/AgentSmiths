from langchain import hub
import os
os.environ["LANGCHAIN_API_KEY"] = "ls__2dffbc675b6e4ca691d5ae45d6a45b40"

def getprompt():
    prompt = hub.pull("rlm/rag-prompt")
    return prompt

if __name__ == "__main__":
    prompt = getprompt()
    print(prompt)