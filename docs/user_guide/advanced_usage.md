
```markdown
# Advanced Usage

This guide covers more advanced features and use cases of the Code Generation Library.

## Custom Templates

You can create your own templates or modify existing ones. Templates are written in Jinja2 format.

1. Create a custom template (e.g., `custom_model.py.jinja2`):

```jinja2
from sqlalchemy import Column, Integer, String
from database import Base

class {{ model_name }}(Base):
    __tablename__ = "{{ model_name|lower }}s"

    id = Column(Integer, primary_key=True, index=True)
    {% for field in fields %}
    {{ field }} = Column(String)
    {% endfor %}

2. Update your config file to include the new template:

yamlCopytemplates:
  custom_model:
    path: "path/to/custom_model.py.jinja2"

3. Use the custom template:

pythonCopygenerator.generate_code('custom_model', 'app/models/custom_user.py', model_name='CustomUser', fields=['name', 'email'])
Batch Generation
You can generate multiple files in a batch:
pythonCopymodels = [
    {'name': 'User', 'fields': ['name', 'email']},
    {'name': 'Product', 'fields': ['name', 'price', 'description']},
    {'name': 'Order', 'fields': ['user_id', 'product_id', 'quantity']}
]

for model in models:
    generator.generate_code('database/model', f'app/models/{model["name"].lower()}.py', model_name=model['name'], fields=model['fields'])
    generator.generate_code('crud/crud_operations', f'app/crud/{model["name"].lower()}.py', model_name=model['name'])
    generator.generate_code('api/router', f'app/api/{model["name"].lower()}.py', model_name=model['name'])
Using Hooks
You can use hooks to modify the generated code before it's written to a file:
pythonCopydef add_copyright(content):
    copyright = "# Copyright (c) 2023 Your Company\n\n"
    return copyright + content

generator.add_hook('post_render', add_copyright)
Now, every generated file will include the copyright notice at the top.
Generating Entire Project Structures
You can use the library to generate entire project structures:
pythonCopyproject_structure = {
    'app': {
        'models': ['user.py', 'product.py', 'order.py'],
        'crud': ['user.py', 'product.py', 'order.py'],
        'api': ['user.py', 'product.py', 'order.py'],
        'core': ['config.py', 'database.py'],
        'main.py': None
    },
    'tests': {
        'test_api': ['test_user.py', 'test_product.py', 'test_order.py'],
        'conftest.py': None
    },
    'alembic': {
        'versions': {},
        'env.py': None,
        'script.py.mako': None
    },
    'requirements.txt': None,
    'README.md': None
}

def generate_project(structure, base_path=''):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            generate_project(value, path)
        elif isinstance(value, list):
            os.makedirs(path, exist_ok=True)
            for file in value:
                generator.generate_code(f'{key}/{file.split(".")[0]}', os.path.join(path, file))
        elif value is None:
            generator.generate_code(key, path)

generate_project(project_structure)
This will generate a complete project structure with all necessary files.
