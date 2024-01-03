from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv
load_dotenv()
google_api_key = os.environ.get("google_api_key")

class agent:
    def __init__(self,template):
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", client="google", google_api_key=google_api_key) #init the model
        # create the prompt template
        self.template = template
        # create the prompt
        self.prompt = ChatPromptTemplate.from_template(self.template)
        # create the output parser
        self.output_parser = StrOutputParser()

    # use the model to make basic query
    def query(self,input_text):
        response = self.llm.invoke(input_text)
        return response

    # use the model to make structred query
    def chainquery(self,input):
        chain = self.prompt | self.llm | self.output_parser
        response = chain.invoke(input)
        return response

class dev_agent(agent):
    def __init__(self):

        #developer template
        self.template = """
        reply with the relevant html , css and js codes to create the following web page of the given project according to the given description:
        project:{project}
        webpage:{webpage}
        description: {description}
        """
        super().__init__(self.template)
