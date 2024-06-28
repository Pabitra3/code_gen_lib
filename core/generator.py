
import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from .template_manager import TemplateManager
from .config_manager import ConfigManager
from ..utils.string_utils import camel_to_snake

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

    def generate_code(self, template_name, output_path, **kwargs):
        try:
            self._validate_inputs(template_name, output_path, **kwargs)
            
            template = self.template_manager.get_template(template_name)
            config = self.config_manager.get_config(template_name)
            
            # Merge kwargs with config, kwargs take precedence
            context = {**config, **kwargs}
            
            # Apply any necessary transformations
            context = self._transform_context(context)
            
            rendered_code = template.render(context)
            
            with open(output_path, 'w') as f:
                f.write(rendered_code)
            
            print(f"Generated code saved to {output_path}")
        except TemplateNotFound:
            raise TemplateError(f"Template not found: {template_name}")
        except (TemplateError, ConfigError, OutputError) as e:
            raise e
        except Exception as e:
            raise CodeGenerationError(f"An unexpected error occurred: {str(e)}")

    def _transform_context(self, context):
        """Apply any necessary transformations to the context."""
        if 'model_name' in context:
            context['model_name_snake'] = camel_to_snake(context['model_name'])
        return context

