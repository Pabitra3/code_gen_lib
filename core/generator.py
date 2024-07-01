
import os
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from .template_manager import TemplateManager
from .config_manager import ConfigManager
from ..utils.string_utils import camel_to_snake
from .exceptions import ConfigError, TemplateError, OutputError

class CodeGenerationError(Exception):
    """Base exception for code generation errors."""
    pass

class TemplateError(CodeGenerationError):
    """Raised when there's an issue with templates."""
    pass

class ConfigError(CodeGenerationError):
    """Raised when there's an issue with configuration."""
    pass

class OutputError(CodeGenerationError):
    """Raised when there's an issue with output operations."""
    pass

class CodeGenerator:
    def __init__(self, config_path):
        """
        Initialize the CodeGenerator.

        Args:
            config_path (str): Path to the configuration file.

        Raises:
            ConfigError: If the configuration file is not found or cannot be loaded.
        """
        self.config = self._load_config(config_path)
        self.template_manager = TemplateManager(self.config.get('template_dirs'))
        if not os.path.exists(config_path):
            raise ConfigError(f"Config file not found: {config_path}")
        
        try:
            self.config_manager = ConfigManager(config_path)
        except Exception as e:
            raise ConfigError(f"Failed to initialize ConfigManager: {str(e)}")
        
        try:
            self.template_manager = TemplateManager()
        except Exception as e:
            raise TemplateError(f"Failed to initialize TemplateManager: {str(e)}")
    def _load_config(self, config_path):
        """
        Load the configuration from a YAML file.

        Args:
            config_path (str): Path to the configuration file.

        Returns:
            dict: Loaded configuration.

        Raises:
            ConfigError: If the configuration file is not found or cannot be loaded.
        """
        try:
            with open(config_path, 'r') as config_file:
                return yaml.safe_load(config_file)
        except FileNotFoundError:
            raise ConfigError(f"Configuration file not found: {config_path}")
        except yaml.YAMLError as e:
            raise ConfigError(f"Error parsing configuration file: {str(e)}")

    def generate_code(self, template_name, output_path, **kwargs):
        """
        Generate code using a template and write it to an output file.

        Args:
            template_name (str): Name of the template to use.
            output_path (str): Path where the generated code will be written.
            **kwargs: Additional context data for the template.

        Raises:
            TemplateError: If there's an error with the template.
            OutputError: If there's an error writing the output file.
        """
        try:
            # Merge kwargs with any template-specific config
            context = {**self.config.get('templates', {}).get(template_name, {}), **kwargs}
            
            # Render the template
            rendered_content = self.template_manager.render_template(template_name, context)
            
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write the rendered content to the output file
            with open(output_path, 'w') as output_file:
                output_file.write(rendered_content)
            
            print(f"Generated code saved to {output_path}")
        
        except TemplateError as e:
            raise TemplateError(f"Error with template '{template_name}': {str(e)}")
        except IOError as e:
            raise OutputError(f"Error writing to output file '{output_path}': {str(e)}")

    def generate_multiple(self, generation_configs):
        """
        Generate multiple code files based on a list of configurations.

        Args:
            generation_configs (list): List of dictionaries, each containing 'template_name', 'output_path', and 'context'.

        Raises:
            TemplateError: If there's an error with any template.
            OutputError: If there's an error writing any output file.
        """
        for config in generation_configs:
            self.generate_code(
                config['template_name'],
                config['output_path'],
                **config.get('context', {})
            )

    def list_available_templates(self):
        """
        List all available templates.

        Returns:
            list: A list of available template names.
        """
        return self.template_manager.list_templates()

    def add_custom_filter(self, name, filter_func):
        """
        Add a custom filter to the template environment.

        Args:
            name (str): Name of the filter.
            filter_func (callable): Function to use as the filter.
        """
        self.template_manager.add_filter(name, filter_func)

    def add_global_variable(self, name, value):
        """
        Add a global variable to the template environment.

        Args:
            name (str): Name of the global variable.
            value: Value of the global variable.
        """
        self.template_manager.add_global(name, value)

    def _validate_inputs(self, template_name, output_path, **kwargs):
        if not isinstance(template_name, str) or not template_name:
            raise ValueError("template_name must be a non-empty string")
        
        if not isinstance(output_path, str) or not output_path:
            raise ValueError("output_path must be a non-empty string")
        
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            raise OutputError(f"Output directory does not exist: {output_dir}")
        
        if os.path.exists(output_path):
            raise OutputError(f"Output file already exists: {output_path}")
        
        required_kwargs = self.config_manager.get_required_kwargs(template_name)
        for kwarg in required_kwargs:
            if kwarg not in kwargs:
                raise ValueError(f"Missing required argument: {kwarg}")
    
    def _transform_context(self, context):
        """Apply any necessary transformations to the context."""
        if 'model_name' in context:
            context['model_name_snake'] = camel_to_snake(context['model_name'])
        return context
    def generate_framework_config(self, framework, output_path, **kwargs):
        template_name = f"framework_configs/{framework}_config"
        self.generate_code(template_name, output_path, **kwargs)