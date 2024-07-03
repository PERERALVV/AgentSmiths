import importlib
import os
import subprocess
import shutil
import asyncio
import json
import re
import time
import signal
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

GET_COMMANDS = getattr(importlib.import_module('core.prompts.dev_ops'), 'GET_COMMANDS')
READMEFILE = getattr(importlib.import_module('core.prompts.dev_ops'), 'READMEFILE')
GET_DESCRIPTION = getattr(importlib.import_module('core.prompts.dev_ops'), 'GET_DESCRIPTION')
GET_COMMANDS_CALL = getattr(importlib.import_module('core.function_calls'), 'GET_COMMANDS')

get_execution_path=getattr(importlib.import_module('const.ProjectConst'), 'get_execution_path')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class execute_command(Action):

    name: str ="ExecuteCommand"
    return_json: bool = False
    function_calls = GET_COMMANDS_CALL

    def __init__(self):
        super().__init__()

    async def run(self,project):
        existing_commands = project.commands
        with open(os.path.join(project.root_path, 'package.json'), 'r',encoding="utf-8") as f:
            json_file = json.load(f)
        
        data={
            "package_dependencies":project.package_dependencies,
            "commands":existing_commands,
            "package_json":json.dumps(json_file,indent=4),

        }
        msg=render_template_with_data(GET_COMMANDS, data)
        LOG.info(msg)
        rsp=await self.ask(msg)
        rsp=self.parse_json(rsp)
        LOG.info(json.dumps(rsp, indent=4))
        existing_commands = rsp
        # project.execution_path = get_execution_path(clientID=project.clientID,project_name=project.name,projectID=project.projectID)
        # # Check if the destination path exists
        # if os.path.exists(project.execution_path):
        #     # Remove the directory and its contents
        #     shutil.rmtree(project.execution_path)
        # shutil.copytree(project.root_path, project.execution_path)
        # LOG.info(f"Directory copied from {project.root_path} to {project.execution_path}")
        if existing_commands is not None:
            data={
                "name": project.name,
                "project_details": project.BaSpecification,
            }
            msg=render_template_with_data(GET_DESCRIPTION, data)
            description= await self.ask(msg)
            LOG.info(description)
            data={
                "commands":existing_commands,
                "name": project.name,
                "system_dependencies": project.system_dependencies,
                "package_dependencies": project.package_dependencies,
                "architecture": project.architecture_desc,
                "description": description
            }
            readme=render_template_with_data(READMEFILE, data)
            with open(os.path.join(project.root_path, 'README.md'), 'w',encoding="utf-8") as f:
                f.write(readme)
            LOG.info(readme)
            LOG.info(f"README.md file created in {project.root_path}")
        #     for command in existing_commands:
        #         # Construct the full path for the command
        #         command_str = command["command"]

        #         try:
        #             default_timeout = 60
        #             if int(command.get("timeout"))/1000 > default_timeout:
        #                 default_timeout=command.get("timeout")
        #                 LOG.info(f"Command {command_str} timeout set to {default_timeout} seconds")
        #             # Execute the command asynchronously with a timeout
        #             process = await asyncio.wait_for(
        #                 asyncio.create_subprocess_shell(
        #                     command_str,
        #                     stdout=asyncio.subprocess.PIPE,
        #                     stderr=asyncio.subprocess.PIPE,
        #                     cwd=project.execution_path,
        #                 ),
        #                 timeout=default_timeout
        #             )

        #             # Wait for the command to complete
        #             stdout, stderr = await process.communicate()

        #             # Optionally, handle the command's output and errors
        #             if process.returncode == 0:
        #                 LOG.info(f"Command {command_str} executed successfully: {stdout.decode()}")
        #             else:
        #                 LOG.info(f"Error executing command {command_str}: {stderr.decode()}")

        #         except asyncio.TimeoutError:
        #             LOG.error(f"Command {command_str} timed out after {default_timeout} seconds")

        # url=self.run_dev_and_get_url()
        # project.host_url=url
        return project
    

    def run_dev_and_get_url(self, timeout_seconds=30):
        """
        Runs the 'npm run dev' command and logs the host URL as soon as it's available.
        After a specified timeout, the process is killed, similar to pressing Ctrl+C in the terminal.
        """
        try:
            # Start the npm command in a separate process
            process = subprocess.Popen(['npm', 'run', 'dev'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Set the alarm for the timeout
            signal.alarm(timeout_seconds)

            # Continuously check the output for the URL
            while True:
                # Read a line from the output
                output = process.stdout.readline()
                LOG.info(output)

                # Check if the line contains the URL
                match = re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', output)
                if match:
                    # Extract and log the URL
                    url = match.group(0)
                    LOG.info(f"Host URL: {url}")
                    # Cancel the alarm
                    signal.alarm(0)
                    break

                # Sleep for a short time before checking again
                time.sleep(1)

        except TimeoutError:
            LOG.info("Process timed out. Killing the process.")
            process.kill()
            # Ensure the process's resources are cleaned up
            process.communicate()
            return None
        except Exception as e:
            LOG.info(f"Error: {e}")
            return None
        else:
            # Ensure the alarm is canceled if the process finishes before the timeout
            signal.alarm(0)
            return url
        

def timeout_handler(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, timeout_handler)

