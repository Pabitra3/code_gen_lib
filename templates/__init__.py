
import os
from typing import List, Dict

# Define the base path for templates
TEMPLATE_BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Define subfolders
TEMPLATE_FOLDERS = ['database', 'framework_configs', 'crud']

def get_template_path(folder: str, template_name: str) -> str:
    """
    Get the full path for a specific template.
    
    :param folder: The subfolder name (database, framework_configs, or crud)
    :param template_name: The name of the template file
    :return: Full path to the template file
    """
    if folder not in TEMPLATE_FOLDERS:
        raise ValueError(f"Invalid folder name. Choose from {TEMPLATE_FOLDERS}")
    
    return os.path.join(TEMPLATE_BASE_PATH, folder, template_name)

def list_templates() -> Dict[str, List[str]]:
    """
    List all available templates in each subfolder.
    
    :return: A dictionary with folder names as keys and lists of template names as values
    """
    templates = {}
    for folder in TEMPLATE_FOLDERS:
        folder_path = os.path.join(TEMPLATE_BASE_PATH, folder)
        templates[folder] = [f for f in os.listdir(folder_path) if f.endswith('.py') or f.endswith('.jinja2')]
    return templates

def read_template(folder: str, template_name: str) -> str:
    """
    Read the content of a specific template.
    
    :param folder: The subfolder name (database, framework_configs, or crud)
    :param template_name: The name of the template file
    :return: The content of the template file as a string
    """
    template_path = get_template_path(folder, template_name)
    with open(template_path, 'r') as file:
        return file.read()

# Version of the templates package
__version__ = '0.1.0'

# Additional information about the package
__author__ = 'Pabitra Kumar Sahoo'
__email__ = 'developersivaay@gmail.com'
__description__ = 'Template management for code generation.'

def get_templates_info():
    """Return a dictionary with information about the templates package."""
    return {
        'version': __version__,
        'author': __author__,
        'email': __email__,
        'description': __description__,
        'available_templates': list_templates()
    }

# Make key functions and variables available when importing the package
__all__ = ['get_template_path', 'list_templates', 'read_template', 'get_templates_info', 'TEMPLATE_FOLDERS']