from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv
load_dotenv()
google_api_key = os.environ.get("google_api_key")


class agent:
    def __init__(self, template, temp=0.1, model="text"):
        if model.lower() == "text":
            self.model = "gemini-pro"
        elif model.lower() == "vision":
            self.model = "gemini-pro-vision"
        self.llm = ChatGoogleGenerativeAI(
            model=self.model, client="google", google_api_key=google_api_key, temperature=temp)  # init the model
        # create the prompt template
        self.template = template
        # create the prompt
        self.prompt = ChatPromptTemplate.from_template(self.template)
        # create the output parser
        self.output_parser = StrOutputParser()

    # use the model to make basic query
    def query(self, input_text):
        response = self.llm.invoke(input_text)
        return response

    # use the model to make structred query
    def chainquery(self, input):
        chain = self.prompt | self.llm | self.output_parser
        response = chain.invoke(input)
        return response


class dev_agent(agent):
    def __init__(self):

        # developer template
        self.template = """
        reply only with the relevant html , css and js codes to create the following web page of the given project description according to the web page description:
        
        project name : {project_name}
        project description:{project_description} and my project will contain the following web pages : {webpage_names}
        webpage :{webpage}
        web page description:{webpage_description}
        
        """
        super().__init__(self.template, 0.1, "text")


class code_checker(agent):
    def __init__(self):
        # developer template
        self.template = """
        analyze the given code and check for bugs and possible improvements and return the modified code:
        *the codes should be complete and ready to run*
        *reply only with the modified code*
        
        code:{code}
        """
        super().__init__(self.template, 0.1, "text")


class planner(agent):
    def __init__(self):
        # developer template
        self.template = """
        create a description for the given webpage of the given project:
        
        *describe the needed webpage asuming you are the client*
        
        project:{project}
        webpage:{webpage}
        """
        super().__init__(self.template, 0.1, "text")


class dev_sup(agent):
    def __init__(self):
        # developer template
        self.template = """
        check if the given codes for the webpage of the given project is correct, complete and aligns with the given description of the webpage when the code is run:
        
        project name : {project_name}
        project description:{project}
        webpage:{webpage}
        web page description:{description}
        code:{code}
        """
        super().__init__(self.template, 0.1, "text")
