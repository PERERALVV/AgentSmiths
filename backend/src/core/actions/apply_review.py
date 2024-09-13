import importlib
import os
import re
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

PATCH_HEADER_PATTERN = re.compile(r"^@@ -(\d+),?(\d+)? \+(\d+),?(\d+)? @@")
GET_HUNKS = getattr(importlib.import_module('utils.track_changes'), 'get_diff_hunks')
GET_FILE_CONTENTS=getattr(importlib.import_module('utils.file_handling'), 'get_file_contents')
LOG= getattr(importlib.import_module('core.logger'), 'log')
class apply_review(Action):

    name:str = "apply_review"
    return_json: bool = False

    # def __init__(self):
    #     super().__init__()

    # if hunks[] is empty and there is a review note this should be handled since could be critical error so send for rework
    async def run(self,project):
        if project.current_sub_task_send_for_review:
            LOG.info('applying review')
            if len(project.current_sub_task_review['hunks']) == 0 and project.current_sub_task_review['review_notes'] is not None:
                project.current_sub_task_send_for_review=True
                LOG.info('no hunks sending for rework')
                return project # we return project here since in this case non of the below should not be executed since there are no hunks to apply review applying is done
            
            if not any(hunk['decision'] != 'Apply' for hunk in project.current_sub_task_review['hunks']): # all hunks are of type apply
                LOG.info('all hunks accepted applying all changes')
                project.update_codebase=True
                project.current_sub_task_send_for_review=False

            else:
                if len(project.current_sub_task_review['hunks'])==1:
                    if project.current_sub_task_review['hunks'][0]['decision']=='Ignore':
                        project.current_sub_task_send_for_review=False
                        #  we put the tasks in an inf loop break if upfate codebase is true
                        LOG.info('ignoring single hunk')

                    elif project.current_sub_task_review['hunks'][0]['decision']=='Rework':
                        project.current_sub_task_send_for_review=True
                        LOG.info('sending for rework')

                else:# can contain all 3 types of hunks
                    hunks_to_apply=[]
                    file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
                    file_name=os.path.basename(file_path)
                    old_content=GET_FILE_CONTENTS(os.path.join(project.root_path,file_path),project.root_path)['content']
                    hunks=GET_HUNKS(file_name,old_content,project.curent_sub_task_code_pending_review['code'])
                    # Filter out hunks with decision 'Ignore' before processing
                    project.current_sub_task_review['hunks'] = [hunk for hunk in project.current_sub_task_review['hunks'] if hunk['decision'] != 'Ignore']
                    
                    for hunk in project.current_sub_task_review['hunks']: # when comming to here there will always be at least one rework hunk
                        if hunk['decision']=='Apply':
                            hunks_to_apply.append(hunks[hunk['number']-1])
                        elif hunk['decision']=='Rework':
                            continue
                        else:
                            raise Exception('invalid decision')
                    new_content = self.apply_diff(file_name, old_content, hunks_to_apply, project.curent_sub_task_code_pending_review['code'])
                    project.curent_sub_task_code_pending_review['code']=new_content
                    LOG.info(f"new content after applying approved hunks: \n{new_content}")
                    project.current_sub_task_send_for_review=True
                    LOG.info('found multiple hunks sending required hunks for rework')
# ===================================================================================================================
# irrespective of all of of these if there are review notes we may have to do further actions as well please study the review notes for the accepted actions
# ===================================================================================================================
        return project


    def apply_diff(self, file_name: str, old_content: str, hunks: list[str], fallback: str):
        """
        Apply the diff to the original file content.

        This uses the internal `_apply_patch` method to apply the
        approved diff hunks to the original file content.

        If patch apply fails, the fallback is the full new file content
        with all the changes applied (as if the reviewer approved everythng).

        :param file_name: name of the file being modified
        :param old_content: old file content
        :param hunks: change hunks from the unified diff
        :param fallback: proposed new file content (with all the changes applied)
        """
        diff = (
            "\n".join(
                [
                    f"--- {file_name}",
                    f"+++ {file_name}",
                ]
                + hunks
            )
            + "\n"
        )
        try:
            fixed_content = self._apply_patch(old_content, diff)
        except Exception as e:
            # This should never happen but if it does, just use the new version from
            # the code_task and hope for the best
            LOG.info(f"Error applying diff: {e}; hoping all changes are valid")
            return fallback

        return fixed_content

    # Adapted from https://gist.github.com/noporpoise/16e731849eb1231e86d78f9dfeca3abc (Public Domain)
    @staticmethod
    def _apply_patch(original: str, patch: str, revert: bool = False):
        """
        Apply a patch to a string to recover a newer version of the string.

        :param original: The original string.
        :param patch: The patch to apply.
        :param revert: If True, treat the original string as the newer version and recover the older string.
        :return: The updated string after applying the patch.
        """
        original_lines = original.splitlines(True)
        patch_lines = patch.splitlines(True)

        updated_text = ""
        index_original = start_line = 0

        # Choose which group of the regex to use based on the revert flag
        match_index, line_sign = (1, "+") if not revert else (3, "-")

        # Skip header lines of the patch
        while index_original < len(patch_lines) and patch_lines[index_original].startswith(("---", "+++")):
            index_original += 1

        while index_original < len(patch_lines):
            match = PATCH_HEADER_PATTERN.match(patch_lines[index_original])
            if not match:
                raise Exception("Bad patch -- regex mismatch [line " + str(index_original) + "]")

            line_number = int(match.group(match_index)) - 1 + (match.group(match_index + 1) == "0")

            if start_line > line_number or line_number > len(original_lines):
                raise Exception("Bad patch -- bad line number [line " + str(index_original) + "]")

            updated_text += "".join(original_lines[start_line:line_number])
            start_line = line_number
            index_original += 1

            while index_original < len(patch_lines) and patch_lines[index_original][0] != "@":
                if index_original + 1 < len(patch_lines) and patch_lines[index_original + 1][0] == "\\":
                    line_content = patch_lines[index_original][:-1]
                    index_original += 2
                else:
                    line_content = patch_lines[index_original]
                    index_original += 1

                if line_content:
                    if line_content[0] == line_sign or line_content[0] == " ":
                        updated_text += line_content[1:]
                    start_line += line_content[0] != line_sign

        updated_text += "".join(original_lines[start_line:])
        return updated_text