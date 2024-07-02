from .core import CodeGenCore, ConfigManager, CodeGenerator, TemplateManager
from .templates import list_templates, read_template, get_template_path
from .utils import create_directory, write_file, camel_to_snake, snake_to_camel

# Version of the code_gen_lib package
__version__ = '0.1.0'

# Additional information about the package
__author__ = 'Pabitra Kumar Sahoo'
__email__ = 'developersivaay@gmail.com'
__description__ = 'A library for generating code based on templates and configurations.'

def get_library_info():
    """Return a dictionary with information about the code_gen_lib package."""
    return {
        'version': __version__,
        'author': __author__,
        'email': __email__,
        'description': __description__
    }

class CodeGenLib:
    """
    Main class for the code generation library, providing a unified interface
    to all major components and functionalities.
    """
    def __init__(self, config_file):
        self.core = CodeGenCore(config_file)

    def generate_code(self, template_name, context):
        """Generate code using the specified template and context."""
        return self.core.generate_code(template_name, context)

    def save_generated_code(self, code, filename):
        """Save the generated code to a file."""
        self.core.save_generated_code(code, filename)

    def get_config_value(self, key):
        """Get a configuration value."""
        return self.core.get_config_value(key)

    def set_config_value(self, key, value):
        """Set a configuration value."""
        self.core.set_config_value(key, value)

    def list_templates(self):
        """List all available templates."""
        return list_templates()

    def read_template(self, folder, template_name):
        """Read the content of a specific template."""
        return read_template(folder, template_name)

    @staticmethod
    def create_directory(path):
        """Create a directory."""
        create_directory(path)

    @staticmethod
    def write_file(path, content):
        """Write content to a file."""
        write_file(path, content)

    @staticmethod
    def camel_to_snake(name):
        """Convert a string from camelCase to snake_case."""
        return camel_to_snake(name)

    @staticmethod
    def snake_to_camel(name):
        """Convert a string from snake_case to camelCase."""
        return snake_to_camel(name)

# Define what should be imported with "from code_gen_lib import *"
__all__ = ['CodeGenLib', 'CodeGenCore', 'ConfigManager', 'CodeGenerator', 'TemplateManager',
           'list_templates', 'read_template', 'get_template_path',
           'create_directory', 'write_file', 'camel_to_snake', 'snake_to_camel',
           'get_library_info']