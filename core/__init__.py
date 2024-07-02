
from .config_manager import ConfigManager
from .generator import CodeGenerator
from .template_manager import TemplateManager

# Version of the core package
__version__ = '0.1.0'

# Additional information about the package
__author__ = 'Pabitra Kumar Sahoo'
__email__ = 'developersivaay@gmail.com'
__description__ = 'Core functionality for the code generation library.'

def get_core_info():
    """Return a dictionary with information about the core package."""
    return {
        'version': __version__,
        'author': __author__,
        'email': __email__,
        'description': __description__
    }

class CodeGenCore:
    """
    A unified interface for the core functionality of the code generation library.
    """
    def __init__(self, config_file):
        self.config_manager = ConfigManager(config_file)
        self.template_manager = TemplateManager()
        self.generator = CodeGenerator(self.config_manager, self.template_manager)

    def generate_code(self, template_name, context):
        """
        Generate code using the specified template and context.
        
        :param template_name: Name of the template to use
        :param context: Dictionary containing context for code generation
        :return: Generated code as a string
        """
        return self.generator.generate_code(template_name, context)

    def save_generated_code(self, code, filename):
        """
        Save the generated code to a file.
        
        :param code: Generated code as a string
        :param filename: Name of the file to save the code to
        """
        self.generator.save_generated_code(code, filename)

    def get_config_value(self, key):
        """
        Get a configuration value.
        
        :param key: Configuration key
        :return: Configuration value
        """
        return self.config_manager.get_config_value(key)

    def set_config_value(self, key, value):
        """
        Set a configuration value.
        
        :param key: Configuration key
        :param value: Configuration value
        """
        self.config_manager.set_config_value(key, value)

    def list_templates(self):
        """
        List all available templates.
        
        :return: List of template names
        """
        return self.template_manager.list_templates()

# Define what should be imported with "from core import *"
__all__ = ['ConfigManager', 'CodeGenerator', 'TemplateManager', 'CodeGenCore', 'get_core_info']