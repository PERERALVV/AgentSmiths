from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv
load_dotenv()
google_api_key = os.environ.get("google_api_key")


class agent:
    def __init__(self, template):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro", client="google", google_api_key=google_api_key)  # init the model
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

    # use the model to make structured query
    def chainquery(self, input):
        chain = self.prompt | self.llm | self.output_parser
        response = chain.invoke(input)
        return response


class dev_agent(agent):
    def __init__(self):

        # developer template
        self.template = """
        reply with the relevant html , css and js codes to create the following web page of the given project according to the given description:
        project:{project}
        webpage:{webpage}
        description: {description}
        """
        super().__init__(self.template)


class formatter:
    def __init__(self, input_string):
        self.input_string = input_string
        self.result_dict = {'html': '', 'css': '', 'js': ''}

    def split_and_recognize(self):
        if not self.input_string:
            return self.result_dict

        delimiter = "///"
        parts = self.input_string.split(delimiter)

        html_part = ""
        css_part = ""
        js_part = ""

        for part in parts:
            if "HTML" in part:
                html_part = part.replace("HTML", "")
            elif "CSS" in part:
                css_part = part.replace("CSS", "")
            elif "JS" in part:
                js_part = part.replace("JS", "")

        self.result_dict['html'] = html_part
        self.result_dict['css'] = css_part
        self.result_dict['js'] = js_part

        return self.result_dict
