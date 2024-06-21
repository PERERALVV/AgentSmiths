from utils.file_handling import build_directory_tree,get_multilevel_directory_contents
import json
# print(build_directory_tree('/code/backend/src/core'))
print(json.dumps(get_multilevel_directory_contents('/code/backend/workspace/6546465465616515362/hondahitha hotels'),indent=4))
# print(get_multilevel_directory_contents('/code/backend/src/core'))

# from const.ProjectConst import get_root
# import os
# print(get_root('clientID2',"homda")) # ../workspace/clientID
# os.makedirs(get_root('clientID2',"homda"), exist_ok=True) # creates ../workspace/clientID
