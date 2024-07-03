# Code Generation Library API Reference

## CodeGenerator

The main class for generating code based on templates and configurations.

### Constructor

```python
CodeGenerator(config_path: str)

config_path: Path to the YAML configuration file.

Methods:
generate
       generate(template_name: str, output_path: str) -> None
Generates code based on a specific template and saves it to the output path.

template_name: Name of the template to use.
output_path: Path where the generated code will be saved.

generate_crud:
          generate_crud(model_name: str, output_dir: str) -> None
Generates CRUD operations for a given model.

model_name: Name of the model for which CRUD operations are generated.
output_dir: Directory where the generated CRUD files will be saved.

setup_database_connection:
       setup_database_connection(db_config: dict, output_path: str) -> None
Generates a database connection setup file based on the provided configuration.

db_config: Dictionary containing database configuration details.
output_path: Path where the generated database connection file will be saved.

configure_framework:
         configure_framework(framework_name: str, config: dict, output_dir: str) -> None
Generates configuration files for a specific web framework.

framework_name: Name of the framework (e.g., 'flask', 'django').
config: Dictionary containing framework-specific configuration details.
output_dir: Directory where the generated framework configuration files will be saved.

ConfigParser
Handles parsing and management of configuration files.

Constructor:
        ConfigParser(config_path: str)

config_path: Path to the YAML configuration file.

Methods:
get_context:
        get_context() -> dict
Returns the current configuration context.

update_context:
         update_context(new_context: dict) -> None
Updates the current configuration context with new values.

new_context: Dictionary containing new configuration values to be added or updated.

TemplateManager
Manages template discovery and retrieval.

Constructor:
       TemplateManager()

Methods:
get_crud_templates:
         get_crud_templates() -> List[str]
Returns a list of available CRUD template names.

get_framework_templates:
            get_framework_templates(framework_name: str) -> List[str]
Returns a list of available template names for a specific framework.

framework_name: Name of the framework (e.g., 'flask', 'django').

Utility Functions
String Utilities
Located in utils/string_utils.py.

camel_to_snake:
       camel_to_snake(name: str) -> str
Converts a camelCase string to snake_case.

snake_to_camel:
        snake_to_camel(name: str) -> str
Converts a snake_case string to camelCase.

pluralize:
      pluralize(word: str) -> str
Returns the plural form of a given word.

File Utilities:
      Located in utils/file_utils.py.

ensure_directory:
        ensure_directory(path: str) -> None

Creates a directory if it doesn't exist.

get_file_content:
        get_file_content(file_path: str) -> str
Reads and returns the content of a file.

write_file_content:
       write_file_content(file_path: str, content: str) -> None