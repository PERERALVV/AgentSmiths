import importlib
Ggemini=getattr(importlib.import_module('routes.llm'), 'Ggemini')
from typing import Any, Dict
import json
import re
class Action:
    """
        Base class for all actions.
        any child class should not have any constructor due to the current way the actions are set
        init this class in child class if you want llm access
    
    """
    name: str
    description: str
    return_json: bool = False
    predictability: float = 0
    goal:str="" #this will be used as the system_instruction in the gemini class
    function_calls:Dict[str, Any]|None=None
    
    def __init__(self):
        self.llm=Ggemini(system_instruction=self.goal,json=self.return_json,temp=self.predictability,tools=self.function_calls)

    async def run(self):
        # should be implemented by the child class
        raise NotImplementedError

    # ask llm with memory
    async def askM(self,msg:str) -> str:
        return self.llm.chatGemini(msg)
    
    async def ask(self,msg:str) -> str:
        return self.llm.getGeminiResponse(msg)
    
    def getmemory(self):
        return self.llm.gethistory()
    
    def setmemory(self,history):
        self.llm.sethistory(history)
    
    
    # @staticmethod
    def parse_json(self,json_str:str)->Dict[str,Any]:
        try:
            json_pattern = r"^```json(.*)```$"
            json_match = re.search(json_pattern, json_str, re.DOTALL | re.MULTILINE)
    
            if json_match is not None:
                jsonArray = json_match.group(1)
                return json.loads(jsonArray.strip())
            else:
                self.parse_std_resp(json_str)
        except json.JSONDecodeError as e:
            def fix_json(s):
                s = s.replace('True', 'true')
                s = s.replace('False', 'false')
                def fix_json_newlines(s):
                    pattern = r'("(?:\\\\n|\\.|[^"\\])*")'

                    def replace_newlines(match):
                        return match.group(1).replace('\n', '\\n')

                    return re.sub(pattern, replace_newlines, s)
                # s = s.replace('`', '"')
                return fix_json_newlines(s)
            print(f"Error decoding JSON: {e}")
            return fix_json(json_str)
    
    def parse_python(self,python_str:str)->Any:
        try:
            python_pattern = r"^```python(.*)```$"
            python_match = re.search(python_pattern, python_str, re.DOTALL | re.MULTILINE)
            pythonArray = python_match.group(1)
            return pythonArray.strip()
        except Exception as e:
            print(f"Error decoding Python: {e}")
            return python_str
    
    def parse_std_resp(self,resp:str)->Any:
        try:
            pattern = r"^```(.*)```$"
            match = re.search(pattern, resp, re.DOTALL | re.MULTILINE)
            if match is None:
                return resp
            pythonArray = match.group(1)
            return pythonArray.strip()
        except Exception as e:
            print(f"Error decoding Python: {e}")
            return resp

    def parse_html(self,python_str:str)->Any:
        try:
            python_pattern = r"^```html(.*)```$"
            python_match = re.search(python_pattern, python_str, re.DOTALL | re.MULTILINE)
            pythonArray = python_match.group(1)
            return pythonArray.strip()
        except Exception as e:
            print(f"Error decoding Python: {e}")
            return python_str
