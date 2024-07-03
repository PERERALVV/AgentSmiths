from pathlib import Path
import os
from typing import Optional, Union
import importlib

IgnoreMatcher = getattr(importlib.import_module('utils.ignore'), 'IgnoreMatcher')
LOG = getattr(importlib.import_module('core.logger'), 'log')

def build_directory_tree(path, prefix='', root_path=None) -> str:
    """Build the directory tree structure in a simplified format.

    :param path: The starting directory path.(should be absolute paths)
    :param prefix: Prefix for the current item, used for recursion.
    :param root_path: The root directory path.(used for recursion)
    :return: A string representation of the directory tree.
    """
    output = ""
    indent = '  '

    if root_path is None:
        root_path = path
    
    matcher = IgnoreMatcher(root_path=root_path)

    if os.path.isdir(path):
        if root_path == path:
            output += '/'
        else:
            dir_name = os.path.basename(path)
            output += f'{prefix}/{dir_name}'

        # List items in the directory
        items = os.listdir(path)
        dirs = []
        files = []
        for item in items:
            item_path = os.path.join(path, item)
            if matcher.ignore(item_path):  # Check if item should be ignored
                continue
            if os.path.isdir(item_path):
                dirs.append(item)
            elif os.path.isfile(item_path):
                files.append(item)
        dirs.sort()
        files.sort()

        if dirs:
            output += '\n'
            for index, dir_item in enumerate(dirs):
                item_path = os.path.join(path, dir_item)
                new_prefix = prefix + indent  # Updated prefix for recursion
                output += build_directory_tree(item_path, new_prefix, root_path)

            if files:
                output += f"{prefix}  {', '.join(files)}\n"

        elif files:
            output += f": {', '.join(files)}\n"
        else:
            output += '\n'

    return output

def update_file(path: str, new_content: Union[str, bytes], project=None):
    """
    Update file with the new content.

    :param path: Full path to the file
    :param new_content: New content to write to the file
    :param project: Optional; a Project object related to the file update. Default is None.

    Any intermediate directories will be created if they don't exist.
    If file is text, it will be written using UTF-8 encoding.
    """
    # Ensure the file is within the project root
    try:
        if project is not None and not Path(path).is_relative_to(project.root_path):
            raise ValueError(f"File path '{path}' is outside of the project root '{project.root_path}'")
    except ValueError as e:
        LOG.info(f"An error occurred: {e}")

    os.makedirs(os.path.dirname(path), exist_ok=True)

    if isinstance(new_content, str):
        file_mode = "w"
        encoding = "utf-8"
    else:
        file_mode = "wb"
        encoding = None

    with open(path, file_mode, encoding=encoding) as file:
        file.write(new_content)
        if project is not None:  # project can be None only in tests
            LOG.info(f"Updated file {path}")
            return True


def get_file_contents(
    path: str, project_root_path: str
) -> dict[str, Union[str, bytes]]:
    """
    Get file content and metadata.

    :param path: Full path to the file
    :param project_root_path: Full path to the project root directory
    :return: Object with the following keys:
        - name: File name
        - path: Relative path to the file
        - content: File content (str or bytes)
        - full_path: Full path to the file

    If file is text, it will be read using UTF-8 encoding and `content`
    will be a Python string. If that fails, it will be treated as a
    binary file and `content` will be a Python bytes object.
    """
    # Normalize the path to avoid issues with different path separators
    full_path = os.path.normpath(path)

    try:
        # Assume it's a text file using UTF-8 encoding
        with open(full_path, "r", encoding="utf-8") as file:
            file_content = file.read()
    except UnicodeDecodeError:
        # If that fails, we'll treat it as a binary file
        with open(full_path, "rb") as file:
            file_content = file.read()
    except NotADirectoryError:
        raise ValueError(f"Path is not a directory: {path}")
    except FileNotFoundError:
        raise ValueError(f"File not found: {full_path}")
    except Exception as e:
        raise ValueError(f"Exception in get_file_contents: {e}")

    file_name = os.path.basename(path)
    relative_path = str(Path(path).parent.relative_to(project_root_path))

    if relative_path == '.':
        relative_path = ''

    return {
        "name": file_name,
        "path": relative_path,
        "content": file_content,
        "full_path": full_path,
        "lines_of_code": len(file_content.splitlines()),
    }


def get_directory_contents(
    directory: str,
    ignore: Optional[list[str]] = None,
) -> list[dict[str, Union[str, bytes]]]:
    """
    Get the content of all files in the given directory.

    :param directory: Full path to the directory to search
    :param ignore: List of files or folders to ignore (optional)
    :return: List of file objects as returned by `get_file_contents`

    See `get_file_contents()` for the details on the output structure
    and how files are read.
    """
    return_array = []

    matcher = IgnoreMatcher(ignore, root_path=directory)

    # Using pathlib.Path.rglob() for recursive file traversal
    for file_path in Path(directory).rglob('*'):
        full_path = str(file_path)
        if matcher.ignore(full_path):
            continue

        return_array.append(get_file_contents(full_path, directory))

    return return_array


def clear_directory(directory: str, ignore: Optional[list[str]] = None):
    """
    Delete all files and directories (except ignored ones) in the given directory.

    :param dir_path: Full path to the directory to clear
    :param ignore: List of files or folders to ignore (optional)
    """
    matcher = IgnoreMatcher(ignore, root_path=directory)

    # Using pathlib.Path.rglob() for recursive file traversal
    for file_path in Path(directory).rglob('*'):
        full_path = str(file_path)
        if matcher.ignore(full_path):
            continue

        try:
            if file_path.is_file():
                os.remove(full_path)
            elif file_path.is_dir():
                os.rmdir(full_path)
        except:  # noqa
            # Gracefully handle some weird edge cases instead of crashing
            pass

def get_multilevel_directory_contents(directory: str, ignore: Optional[list[str]] = None) -> list[dict[str, Union[str, bytes]]]:
    """
    Get the content of all files in the given directory, including subdirectories.

    :param directory: Full path to the directory to search
    :param ignore: List of files or folders to ignore (optional)
    :return: List of file objects as returned by `get_file_contents`
    """
    all_files = []
    matcher = IgnoreMatcher(ignore, root_path=directory)
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            if matcher.ignore(full_path):
                continue
            all_files.append(get_file_contents(full_path, directory))
    return all_files