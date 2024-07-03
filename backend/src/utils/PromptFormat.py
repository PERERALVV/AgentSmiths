import importlib
from jinja2 import Environment, FileSystemLoader
import copy
UTILS = getattr(importlib.import_module('core.prompts.utils'), 'UTILS')

def render_template_with_data(tem, Odata):
    data=copy.deepcopy(Odata)
    env = Environment(loader=FileSystemLoader('.'))
    data.update(UTILS)
    intermediate_tem=env.from_string(tem).render(data)
    rendered_template_final = env.from_string(intermediate_tem).render(Odata)
    return rendered_template_final