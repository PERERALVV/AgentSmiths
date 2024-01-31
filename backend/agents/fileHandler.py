import os

def create_directory(path, dir_name):
    dir_path = os.path.join(path, dir_name)
    os.makedirs(dir_path, exist_ok=True)

# Usage
# create_directory("/home/user", "new_directory")


def write_string_to_file(filename, filetype, string):
    with open(f"{filename}.{filetype}", "a") as file:
        file.write(f"\n{string}")

# Usage
# write_string_to_file("test", "txt", "Hello, World!")