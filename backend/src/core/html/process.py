import importlib
import copy
LOG = getattr(importlib.import_module('core.logger'), 'log')
get_root=getattr(importlib.import_module('const.ProjectConst'), 'get_root_html')
develop_plan=getattr(importlib.import_module('core.html.develop_plan'), 'develop_plan')()
code_files=getattr(importlib.import_module('core.html.code_files'), 'code_files')

async def start(WEBSITE,name,user_id,project_id,pages):
    WEBSITE.name=name
    WEBSITE.user_id=user_id
    WEBSITE.project_id=project_id
    WEBSITE.pages=pages
    WEBSITE.root_path=get_root(clientID=WEBSITE.user_id,projectID=WEBSITE.project_id,project_name=WEBSITE.name)

    result = await develop_plan.run(WEBSITE)
    result.file_names=[item['page_name'] for item in result.dev_plan]
    LOG.info(result.file_names)
    # tasks=[]
    for i in range(0, len(WEBSITE.dev_plan), 2):
        website=copy.deepcopy(result)
        # website.pages = WEBSITE.pages[i:i+2]
        website.dev_plan = WEBSITE.dev_plan[i:i+2]
        await code_files().run(website)