
```markdown
# CRUD Templates

This library provides templates for generating CRUD (Create, Read, Update, Delete) operations. These templates are designed to work with SQLAlchemy and can be easily customized to fit your project's needs.

## Available Templates

### crud_operations.py.jinja2

This template generates a set of CRUD functions for a given model.

#### Usage

```python
generator.generate_code('crud/crud_operations', 'output/user_crud.py', model_name='User', fields=['id', 'name', 'email'])