# import asyncio
# from metagpt.logs import logger
# from metagpt.team import Team
# import json



# # this is aquired by the answers for the predined questions(maybe use checkbox or list kind of thing without NL)
# initial_user_requirement_json = []
# logger.info(f"initial_user_requirement_json: {initial_user_requirement_json}")

# idea:str =json.dumps(initial_user_requirement_json)
# logger.info(f"idea: {idea}")


# team = Team()
# team.hire(
#     [

#     ]
# )

# investment: float = 3.0 #maybe modify this by payent plan or customer pririty??just a possible futire upgrade
# n_round: int = 500 #dummy val to keep the loop runing(so only will be stoped due to lack of funds) 

# team.invest(investment=investment)
# team.run_project(idea)
# asyncio.run(team.run(n_round=n_round))
