# TemplateManager API Reference

The `TemplateManager` class is responsible for managing templates in the CodeGenLib library. It provides methods for listing available templates, retrieving template content, and managing template directories.

## Table of Contents

1. [Class Definition](#class-definition)
2. [Methods](#methods)
   - [__init__](#__init__)
   - [list_templates](#list_templates)
   - [get_template_content](#get_template_content)
   - [add_template_directory](#add_template_directory)
   - [remove_template_directory](#remove_template_directory)
3. [Exceptions](#exceptions)
4. [Usage Examples](#usage-examples)

## Class Definition

```python
class TemplateManager:
    """
    Manages templates for code generation.
    """


Methods
init
def __init__(self, template_dir: str = 'templates'):
    """
    Initialize the TemplateManager.

    Args:
        template_dir (str): The base directory for templates. Defaults to 'templates'.
    """
Initializes a new instance of the TemplateManager class.
Parameters:

template_dir (str, optional): The base directory for templates. Defaults to 'templates'.

Raises:

FileNotFoundError: If the specified template directory does not exist.


list_templates
def list_templates(self) -> List[str]:
    """
    List all available templates.

    Returns:
        List[str]: A list of template names.
    """
Returns a list of all available template names.
Returns:

List[str]: A list of template names.


get_template_content
def get_template_content(self, template_name: str) -> str:
    """
    Retrieve the content of a specific template.

    Args:
        template_name (str): The name of the template.

    Returns:
        str: The content of the template.

    Raises:
        TemplateNotFoundError: If the specified template is not found.
    """
Retrieves the content of a specific template.
Parameters:

template_name (str): The name of the template.

Returns:

str: The content of the template.

Raises:

TemplateNotFoundError: If the specified template is not found.


add_template_directory
def add_template_directory(self, directory: str) -> None:
    """
    Add a new directory to search for templates.

    Args:
        directory (str): The path to the new template directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
    """
Adds a new directory to search for templates.
Parameters:

directory (str): The path to the new template directory.

Raises:

FileNotFoundError: If the specified directory does not exist.


remove_template_directory
def remove_template_directory(self, directory: str) -> None:
    """
    Remove a directory from the list of template directories.

    Args:
        directory (str): The path to the template directory to remove.

    Raises:
        ValueError: If the specified directory is not in the list of template directories.
    """
Removes a directory from the list of template directories.
Parameters:

directory (str): The path to the template directory to remove.

Raises:

ValueError: If the specified directory is not in the list of template directories.

Exceptions

TemplateNotFoundError: Raised when a specified template is not found.
FileNotFoundError: Raised when a specified directory does not exist.
ValueError: Raised when trying to remove a directory that is not in the list of template directories.

Usage Examples
Initializing TemplateManager
from code_gen_lib.core import TemplateManager

# Initialize with default template directory
template_manager = TemplateManager()

# Initialize with custom template directory
custom_template_manager = TemplateManager('/path/to/custom/templates')

Listing Templates
templates = template_manager.list_templates()
print(f"Available templates: {templates}")

Getting Template Content
try:
    content = template_manager.get_template_content('my_template.py')
    print(f"Template content:\n{content}")
except TemplateNotFoundError as e:
    print(f"Error: {e}")


Adding a Template Directory
try:
    template_manager.add_template_directory('/path/to/additional/templates')
    print("Template directory added successfully")
except FileNotFoundError as e:
    print(f"Error: {e}")

Removing a Template Directory
try:
    template_manager.remove_template_directory('/path/to/additional/templates')
    print("Template directory removed successfully")
except ValueError as e:
    print(f"Error: {e}")


This API reference provides developers with a comprehensive guide to using the TemplateManager class in your CodeGenLib library. It includes detailed information about each method, including parameters, return values, and potential exceptions. The usage examples demonstrate how to use each method in practice.
