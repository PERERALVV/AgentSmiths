from routes.llm import Ggemini
from database.vecDB import getDB
import textwrap
from core.prompts.SupportBot import PURPOSE
import importlib
send_db=getattr(importlib.import_module('database.database'), 'store_chat')
class chatbot:
    def __init__(self,sid):
        self.chat_history = []
        self.sid=sid
        self.llm=Ggemini(PURPOSE)
    def make_prompt(self,query, relevant_passage):
        # TODO:IMPOROVEMNT: use lllm to reprase user msg depending on chat history(ex:"how can i use it?" -> "how to use Agentsmiths?")
        escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
        prompt = textwrap.dedent("""       
        USER QUESTION: '{query}'
        PASSAGE: '{relevant_passage}'

        YOUR ANSWER:
        """).format(query=query, relevant_passage=escaped)

        return prompt

    # TODO: make this function async and handle any potentional errors that may occur  
    async def bot_chat(self,user_input):
        db=getDB()
        query=user_input
        passage = db.query(query_texts=[query], n_results=1)['documents'][0]
        relevant_text = passage[0]
        reply=self.llm.chatGemini(self.make_prompt(query,relevant_text))
        # print(reply)
        # print("chatbot: ",relevant_text)
        self.chat_history.append({"user":query})
        self.chat_history.append({"bot":reply})
        
        return reply

    async def bot_init(self):
        if len(self.chat_history)>1:
            # this is just for safety, should not be needed
            await send_db(self.sid,self.chat_history)
            
            
        self.chat_history=[{"bot":"Hello, have a question about AgentSmiths? Ask me anything!"}]

    async def bot_close(self):
        if len(self.chat_history)!=0:
            
            if len(self.chat_history)==1:
    # users opennig the bot but not using handled here
                return
            await send_db(self.sid,self.chat_history)
            
            self.chat_history=[]
    
    async def connect_human(self):
        await send_db(self.sid,self.chat_history,True)
        print("connect human done")
        self.chat_history=[]

if __name__ == "__main__":
    chat_history = []