import os
from typing import Optional , Any
from uuid import uuid4



from .javascript_react import JAVASCRIPT_REACT
from .node_express_mongoose import NODE_EXPRESS_MONGOOSE
from .render import Renderer


PROJECT_TEMPLATES = {
    "node_express_mongoose": NODE_EXPRESS_MONGOOSE,
    "javascript_react": JAVASCRIPT_REACT,
}


def apply_project_template(
    project
):
    """
    Apply a project template to a new project.

    :param project: the project object
    :return: a summary of the applied template, or None if no template was applied

    If project.project_template is None (not selected), or not one of the supported
    templates, do nothing.

    Note: the template summary is injected in the project description, and the
    created files are saved to a snapshot of the last development step (LLM request).
    """
    template_name = project.template_name
    if not template_name or template_name not in PROJECT_TEMPLATES:
        print(f"Project template '{template_name}' not found, ignoring")
        return None

    root_path = project.root_path
    project_name = project.name
    project_description = project.architecture_desc
    template = PROJECT_TEMPLATES[template_name]
    install_hook = template.get("install_hook")#this has the command to install npm | this can be removed i think!

    #######################################################################################################
    ## the important vars in here are template and the project_files
    #######################################################################################################
    r = Renderer(
        os.path.join(os.path.dirname(__file__), "tpl")
    )

    files = r.render_tree(
        template["path"],
        {
            "project_name": project_name,
            "project_description": project_description,
            "random_secret": uuid4().hex,
        },
    )

    project_files = []

    for file_name, file_content in files.items():
        full_path = os.path.join(root_path, file_name)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(file_content)

        rel_dir = os.path.dirname(file_name)
        project_files.append({
            "name": os.path.basename(file_name),
             # ensure the path is compatible with how the rest of project thinks about paths
            "path": "/" if rel_dir in ["", "."] else rel_dir,
            "content": file_content,
        })

    project.template_project_files = project_files
    project.template_obj = template
    return project
