# Customizing Templates in CodeGenLib

This guide will walk you through the process of customizing templates in CodeGenLib. Templates are the backbone of our code generation system, allowing you to create flexible, reusable patterns for generating code.

## Table of Contents

1. [Understanding Templates](#understanding-templates)
2. [Template Structure](#template-structure)
3. [Creating a New Template](#creating-a-new-template)
4. [Modifying Existing Templates](#modifying-existing-templates)
5. [Using Variables in Templates](#using-variables-in-templates)
6. [Advanced Template Techniques](#advanced-template-techniques)
7. [Best Practices](#best-practices)

## Understanding Templates

Templates in CodeGenLib are files that contain the structure of the code you want to generate, along with placeholders for dynamic content. We use the Jinja2 templating engine, which provides a powerful and flexible way to create templates.

## Template Structure

Templates are organized in the `templates` folder of the CodeGenLib package. This folder contains subfolders for different types of templates:

- `database`: Templates for database-related code
- `framework_configs`: Templates for framework configuration files
- `crud`: Templates for CRUD operations

Each template is a `.py` or `.jinja2` file that contains Python code with Jinja2 syntax for dynamic parts.

## Creating a New Template

To create a new template:

1. Choose the appropriate subfolder in the `templates` directory.
2. Create a new file with a `.py` or `.jinja2` extension.
3. Write your template using Python code and Jinja2 syntax.

Example of a simple CRUD template (`templates/crud/simple_crud.py`):

```python
class {{ model_name }}:
    def __init__(self, {% for field in fields %}{{ field }}{% if not loop.last %}, {% endif %}{% endfor %}):
        {% for field in fields %}
        self.{{ field }} = {{ field }}
        {% endfor %}

    def create(self):
        # Implementation for creating a new {{ model_name }}
        pass

    def read(self, id):
        # Implementation for reading a {{ model_name }}
        pass

    def update(self):
        # Implementation for updating a {{ model_name }}
        pass

    def delete(self):
        # Implementation for deleting a {{ model_name }}
        pass