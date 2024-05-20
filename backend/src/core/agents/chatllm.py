from routes.llm import Ggemini

class chatllm:
    
    def __init__(self):
        self.llm = Ggemini()
    
    def talk(self,msg):
        response=self.llm.getGeminiResponse(msg)
        return response