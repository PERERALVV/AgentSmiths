import importlib
import os
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

ASK_QUESTIONS= getattr(importlib.import_module('core.prompts.buisness_analyst'), 'ASK_QUESTIONS')
ASK_QUESTIONS_CALL = getattr(importlib.import_module('core.function_calls'), 'ASK_QUESTIONS')
SPEC_RECORRECT= getattr(importlib.import_module('core.prompts.buisness_analyst'), 'SPEC_RECORRECT')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class ask_questions(Action):

    name:str = "ask_questions"
    return_json: bool = False
    goal: str = ASK_QUESTIONS
    function_calls = ASK_QUESTIONS_CALL

    def __init__(self):
        # self.initial_convo=initial_convo
        super().__init__()

    async def run(self,project):
        if project.Spec_review is None:# initial question round
            memory = [
                part for item in project.user_convo for part in [
                    {"role": "model", "parts": [item["question"]]},
                    {"role": "user", "parts": [item["answer"]]}
                ]
            ]
            project.user_convo = [{"question": self.parse_json(item["question"])["content"] , "answer":item['answer']} for item in project.user_convo]
            LOG.info(project.user_convo)
            self.setmemory(memory)
            msg=project.user_convo[-1]['answer']
            rsp=await self.askM(msg)
            rsp=self.parse_json(rsp)
            while rsp['state']=="Question":
                project.user_convo.append({"question":rsp['content'],"answer":""})
            #====================================================================================================================================================
            # ==============this code should be in gayunis code and it should be called from here instead of sio take that as param==============================
                # try:
                #     # msg = await sio.call('send_message', {"message":rsp['content']},timeout=120,to=project.clientID)
                #     msg = input("Enter your response: ")
                # except Exception as e:
                #     LOG.error(f"Error in sending message: {e}")
                msg= await project.user_connection(rsp['content'],project.projectID)
            #====================================================================================================================================================
                project.user_convo[-1]['answer']=msg
                rsp=await self.askM(msg)
                rsp=self.parse_json(rsp)
                LOG.info(project.user_convo)
                # LOG.info(self.getmemory())
            project.BaSpecification=rsp['content']
            LOG.info(f"specification:\n{project.BaSpecification}")
        else:
            data={
                "missinginfo":project.Spec_review
            }
            msg=render_template_with_data(SPEC_RECORRECT, data)
            rsp=await self.askM(msg)
            rsp=self.parse_json(rsp)
            LOG.info(rsp)

            while rsp['state']=="Question":
                project.user_convo.append({"question":rsp['content'],"answer":""})
                LOG.info(project.user_convo)
            #====================================================================================================================================================
            # ==============this code should be in gayunis code and it should be called from here instead of sio take that as param==============================
                # try:
                #     # msg = await sio.call('send_message', {"message":rsp['content']},timeout=120,to=project.clientID)
                #     msg = input("Enter your response: ")
                # except Exception as e:
                #     LOG.error(f"Error in sending message: {e}")
                msg= await project.user_connection(rsp['content'],project.projectID)
            #====================================================================================================================================================
                project.user_convo[-1]['answer']=msg
                rsp=await self.askM(msg)
                rsp=self.parse_json(rsp)
                LOG.info(project.user_convo)
            project.BaSpecification=rsp['content']
            LOG.info(f"specification:\n{project.BaSpecification}")
        return project
