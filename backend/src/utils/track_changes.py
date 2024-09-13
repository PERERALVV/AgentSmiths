import os
import subprocess

def init_git_tracking(folder_path):
    """
    Initializes Git tracking in the specified folder.

    Args:
        folder_path (str): The path to the folder.
    """
    os.chdir(folder_path)  # Change directory to the folder
    subprocess.run(['git', 'init'])  # Initialize Git repository
    subprocess.run(['git', 'add', '.'])  # Add all files to staging area
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])  # Commit the initial state

def reset_git_tracking(folder_path):
    """
    Resets Git tracking to the last commit in the specified folder.

    Args:
        folder_path (str): The path to the folder.
    """
    os.chdir(folder_path)  # Change directory to the folder
    subprocess.run(['git', 'reset', '--hard', 'HEAD'])  # Reset to last commit
def create_commit(folder_path, commit_message):
    """
    Creates a new Git commit in the specified folder with the given message.
    """
    os.chdir(folder_path)
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_message])

def show_git_changes(folder_path):
    """
    Displays the changes made since the last commit in the specified folder as a list of hunks.
    """
    os.chdir(folder_path)
    process = subprocess.run(['git', 'diff', 'HEAD'], capture_output=True, text=True)
    diff_output = process.stdout.strip()

    hunks = []
    current_hunk = []
    for line in diff_output.splitlines():
        if line.startswith("+++ b/"):  # Start of a new hunk
            if current_hunk:  # Add previous hunk if not empty
                hunks.append(current_hunk)
            current_hunk = [line]
        elif current_hunk:
            current_hunk.append(line)

    if current_hunk:  # Add the last hunk
        hunks.append(current_hunk)

    return hunks

from difflib import unified_diff
import re

def get_diff_hunks(file_name: str, old_content: str, new_content: str) -> list[str]:
    """
    Get the diff between two files.

    This uses Python difflib to produce an unified diff, then splits
    it into hunks that will be separately reviewed by the reviewer.

    :param file_name: name of the file being modified
    :param old_content: old file content
    :param new_content: new file content
    :return: change hunks from the unified diff
    """
    from_name = "old_" + file_name
    to_name = "to_" + file_name
    from_lines = old_content.splitlines(keepends=True)
    to_lines = new_content.splitlines(keepends=True)
    diff_gen = unified_diff(from_lines, to_lines, fromfile=from_name, tofile=to_name)
    diff_txt = "".join(diff_gen)

    hunks = re.split(r"\n@@", diff_txt, re.MULTILINE)
    result = []
    for i, h in enumerate(hunks):
        # Skip the prologue (file names)
        if i == 0:
            continue
        txt = h.splitlines()
        txt[0] = "@@" + txt[0]
        result.append("\n".join(txt))
    return result
