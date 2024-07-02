```markdown
# Configuration Options

The Code Generation Library uses a YAML configuration file for customization. Here's a detailed look at the available options:

## Basic Structure

```yaml
database:
  url: "sqlite:///./test.db"

templates:
  model:
    path: "templates/database/model.py.jinja2"
  crud:
    path: "templates/crud/crud_operations.py.jinja2"
  api:
    path: "templates/api/router.py.jinja2"

hooks:
  pre_render: []
  post_render: []

output:
  base_dir: "./output"