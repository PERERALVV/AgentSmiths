import json ,re
from routes.llm import Ggemini
import importlib

ProjectConst = importlib.import_module('const.ProjectConst')
USE_JSON = getattr(ProjectConst, 'USE_JSON')
STATIC_SITES = getattr(ProjectConst, 'STATIC_SITES')
# end_conversation=getattr(importlib.import_module("routes.api"),"end_conversation")
BAoverload = importlib.import_module('core.agents.BAoverload')
BAoverload = getattr(BAoverload, 'BAoverload')

# from core.prompts.ask_questions import ASKQUESTIONS1, ASKQUESTIONS2  #this also worked useed below just for fun
questions = importlib.import_module('core.prompts.ask_questions')
ASKQUESTIONS1 = getattr(questions, 'ASKQUESTIONS1')
ASKQUESTIONS2 = getattr(questions, 'ASKQUESTIONS2')
ASKQUESTIONS2_JSON = getattr(questions, 'ASKQUESTIONS2_JSON')
ASKQUESTIONS1static = getattr(questions, 'ASKQUESTIONS1static')
ASKQUESTIONS2static = getattr(questions, 'ASKQUESTIONS2static')
BApurpose = getattr(questions, 'BApurpose')
RESPEC = getattr(questions, 'RESPEC')

# TODO : MAKE this fucntion to retrun array as [type,content] where type is either specification or question then all the interactons can be doen in parent/outside fucntion so ba overkload will be called in tht outside one
class BA:
    name:str ="Minu"
    profile:str="Business Analyst"

    def __init__(self,sio,techstack:str="JAVASCRIPT/REACT",frontend:str="REACT with Styled components",initquestion:str="put your question here"):
        if USE_JSON:
            self.sysprompt=BApurpose+ASKQUESTIONS1.format(techstack=techstack,frontend=frontend)+ASKQUESTIONS2_JSON
        elif STATIC_SITES:
            self.sysprompt=BApurpose+ASKQUESTIONS1static.format(techstack="HTML/CSS/JAVASCRIPT",frontend="Bootstrap STYLES")+ASKQUESTIONS2static
        else:
            self.sysprompt=BApurpose+ASKQUESTIONS1.format(techstack=techstack,frontend=frontend)+ASKQUESTIONS2
        # print(self.sysprompt)
        self.llm = Ggemini(self.sysprompt,json=USE_JSON)
        self.reviewer=BAoverload()
        self.convo=[{"question":initquestion,"answer":""}]
        self.sio=sio
        if USE_JSON:
            self.parse=self.parse_json
        else:
            self.parse=self.parse_non_json
    
    async def consult(self,msg:str,client:bool=True)->str:
        # TODO: analyze the client's response if its a simple one no need to create complex specification(can send straight to dev)
        if client:
            self.convo[-1]["answer"]=msg
        print(json.dumps(self.convo, indent=4))
        for _ in range(3):  # retry up to 3 times
            try:
                response = self.llm.chatGemini(msg)
                print(response)
                # await self.sio.emit("end_conversation")# for testing
                jsonobj = self.parse(response)
                break  # if the above lines succeed, break the loop
            except Exception as e:
                print(f"An error occurred: {e}. Retrying...")
        else:
            print("Failed to get a valid response after 3 attempts.")

        # if gemini json parameter is set to True this will convert the spec to a legacy compatible mode
        if USE_JSON and jsonobj["state"]=="specification":
            jsonobj=json.dumps(jsonobj["specification"])
        
        if isinstance(jsonobj, str):
            print(jsonobj)
            review=self.reviewer.consult( jsonobj , json.dumps(self.convo) )
            if review is not None:
                if review[0] == "MISSING-INFORMATION":
                    selfmsg = RESPEC.format(MISSINGINFO=review[1])
                    resp = await self.consult(selfmsg,False)
                    if resp != "":
                        return resp
                    print("missing information")
                # elif review[0] == "NO-MISSING-INFORMATION":
                else:
                    print("---------------------------------------------------------------done-----------------------------------------------------------------------------------------------")
                    # TODO: call gayuinis function to note end of questions
                    # TODO: to next agent here
                    await sio.emit("end_conversation")
                    print(jsonobj)
                    with open("my_file.txt", "w") as file:
                        file.write(jsonobj)
                    return ""
            else:
                # TODO: may need to send to next agent from here too 
                await sio.emit("end_conversation")
                print(jsonobj)
                with open("my_file.txt", "w") as file:
                    file.write(jsonobj)
                print("returned since baoverload returned None")
                return ""
                # return jsonobj
                # print(jsonobj)
        elif isinstance(jsonobj, dict):
            self.convo.append({"question":jsonobj["question"],"answer":""})
            # print(json.dumps(jsonobj, indent=4))
            return jsonobj["question"]
        elif jsonobj is None:
            print("Error: jsonobj is None")
            return ""
    
    @staticmethod
    def parse_non_json(rsp:str)->dict:
        json_pattern = r"^```json(.*)```$"
        spec_pattern = r"^```specification(.*)```$"
        json_match = re.search(json_pattern, rsp, re.DOTALL | re.MULTILINE)
        spec_match = re.search(spec_pattern, rsp, re.DOTALL | re.MULTILINE)
        
        if json_match:
            jsonArray = json_match.group(1)
            return json.loads(jsonArray.strip())
        elif spec_match:
            return spec_match.group(1).strip()
        else:
            return None
        
    
    @staticmethod
    def parse_json(rsp:str):
        try:
            return eval(rsp)
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
            return fix_json(rsp)

# ba=BA()

# res=ba.consult("i want to build a website for my grocery store")
# print(res)
# while True:
#     inp=input("asn: ")
#     res=ba.consult(inp)
#     print(res)