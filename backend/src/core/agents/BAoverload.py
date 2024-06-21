from routes.llm import Ggemini
import importlib
import json ,re

ProjectConst = importlib.import_module('const.ProjectConst')
STATIC_SITES = getattr(ProjectConst, 'STATIC_SITES')

questions = importlib.import_module('core.prompts.review_specs')
RVSPEC = getattr(questions, 'RVSPEC')
RVSPECstatic = getattr(questions, 'RVSPECstatic')

class BAoverload:
    name:str ="shaniya"
    profile:str="Business Analyst reviewere"

    def __init__(self):
        self.llm = Ggemini("")
        
    
    def consult(self,spec:str,convo:str)->str:
        if STATIC_SITES:
            msg=RVSPECstatic.format(spec=spec,convo=convo)
        else:
            msg=RVSPEC.format(spec=spec,convo=convo)
        # print(msg)
        response = self.llm.getGeminiResponse(msg)
        parsed_response=self.parse_json(response)
        print(parsed_response)
        return parsed_response
    
    @staticmethod
    def parse_json(rsp:str)->dict:
        missing_pattern = r"^```MISSING-INFORMATION(.*)```$"
        not_missing_pattern = r"^```NO-MISSING-INFORMATION(.*)```$"
        json_match = re.search(missing_pattern, rsp, re.DOTALL | re.MULTILINE)
        spec_match = re.search(not_missing_pattern, rsp, re.DOTALL | re.MULTILINE)
        
        if json_match:
            return ["MISSING-INFORMATION",json_match.group(1).strip()]
        elif spec_match:
            return ["NO-MISSING-INFORMATION",spec_match.group(1).strip()]
        else:
            return None