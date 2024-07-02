# CodeGenerator Class

The `CodeGenerator` class is the main interface for generating code using this library.

## Constructor

### `CodeGenerator(config_path: str)`

Creates a new `CodeGenerator` instance.

#### Parameters:
- `config_path` (str): Path to the configuration file.

#### Raises:
- `ConfigError`: If the configuration file is not found or cannot be loaded.

## Methods

### `generate_code(template_name: str, output_path: str, **kwargs) -> None`

Generates code based on the specified template and saves it to the output path.

#### Parameters:
- `template_name` (str): Name of the template to use.
- `output_path` (str): Path where the generated code will be saved.
- `**kwargs`: Additional keyword arguments to be passed to the template.

#### Raises:
- `TemplateError`: If the specified template is not found.
- `ConfigError`: If there's an issue with the configuration for the template.
- `OutputError`: If there's an issue writing to the output path.
- `CodeGenerationError`: For any other unexpected errors during code generation.

### `generate_framework_config(framework: str, output_path: str, **kwargs) -> None`

Generates a configuration file for the specified framework.

#### Parameters:
- `framework` (str): Name of the framework (e.g., 'flask', 'django', 'fastapi').
- `output_path` (str): Path where the generated configuration will be saved.
- `**kwargs`: Framework-specific configuration options.

#### Raises:
- Same exceptions as `generate_code()`.

## Examples

```python
# Initialize the generator
generator = CodeGenerator('path/to/config.yaml')

# Generate CRUD operations
generator.generate_code('crud/create', 'output/create_user.py', model_name='User', fields=['id', 'name', 'email'])

# Generate a Flask configuration
generator.generate_framework_config('flask', 'config.py', secret_key='your-secret-key', dev_database_name='dev_db')