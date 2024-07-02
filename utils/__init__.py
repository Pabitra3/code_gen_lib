# utils/__init__.py

# Import functions from file_operations.py
from .file_operations import create_directory, write_file

# Import functions from string_utils.py
from .string_utils import camel_to_snake, snake_to_camel

# You can optionally define __all__ to specify what gets imported with "from utils import *"
__all__ = ['create_directory', 'write_file', 'camel_to_snake', 'snake_to_camel']

# Version of the utils package
__version__ = '0.1.0'

# Additional information about the package
__author__ = 'Pabitra Kumar Sahoo'
__email__ = 'developersivaay@gmail.com'
__description__ = 'My Custom Python Library for Automated Code Generation'

def get_utils_info():
    """Return a dictionary with information about the utils package."""
    return {
        'version': __version__,
        'author': __author__,
        'email': __email__,
        'description': __description__
    }