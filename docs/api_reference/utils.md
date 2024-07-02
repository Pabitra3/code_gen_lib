# Utils API Reference

The `utils` module provides a collection of utility functions that are used throughout the CodeGenLib library. These functions offer common operations for file handling, string manipulation, and other general-purpose tasks.

## Table of Contents

1. [File Operations](#file-operations)
   - [create_directory](#create_directory)
   - [write_file](#write_file)
2. [String Utilities](#string-utilities)
   - [camel_to_snake](#camel_to_snake)
   - [snake_to_camel](#snake_to_camel)
3. [Usage Examples](#usage-examples)

## File Operations

### create_directory

```python
def create_directory(path: str) -> None:
    """
    Create a directory if it doesn't exist.

    Args:
        path (str): The path of the directory to create.

    Raises:
        OSError: If the directory cannot be created.
    """


Creates a directory if it doesn't already exist.
Parameters:

path (str): The path of the directory to create.

Raises:

OSError: If the directory cannot be created.


write_file
def write_file(path: str, content: str) -> None:
    """
    Write content to a file.

    Args:
        path (str): The path of the file to write.
        content (str): The content to write to the file.

    Raises:
        IOError: If the file cannot be written.
    """
Writes content to a file.
Parameters:

path (str): The path of the file to write.
content (str): The content to write to the file.

Raises:

IOError: If the file cannot be written.

String Utilities
camel_to_snake
def camel_to_snake(name: str) -> str:
    """
    Convert a camelCase string to snake_case.

    Args:
        name (str): The camelCase string to convert.

    Returns:
        str: The converted snake_case string.
    """
Converts a camelCase string to snake_case.
Parameters:

name (str): The camelCase string to convert.

Returns:

str: The converted snake_case string.


snake_to_camel
def snake_to_camel(name: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
        name (str): The snake_case string to convert.

    Returns:
        str: The converted camelCase string.
    """
Converts a snake_case string to camelCase.
Parameters:

name (str): The snake_case string to convert.

Returns:

str: The converted camelCase string.

Usage Examples

File Operations
from code_gen_lib.utils import create_directory, write_file

# Creating a directory
try:
    create_directory('/path/to/new/directory')
    print("Directory created successfully")
except OSError as e:
    print(f"Error creating directory: {e}")

# Writing to a file
try:
    write_file('/path/to/file.txt', 'Hello, World!')
    print("File written successfully")
except IOError as e:
    print(f"Error writing file: {e}")

String Utilities
from code_gen_lib.utils import camel_to_snake, snake_to_camel

# Converting camelCase to snake_case
camel_str = "myVariableName"
snake_str = camel_to_snake(camel_str)
print(f"camelCase: {camel_str} -> snake_case: {snake_str}")

# Converting snake_case to camelCase
snake_str = "my_variable_name"
camel_str = snake_to_camel(snake_str)
print(f"snake_case: {snake_str} -> camelCase: {camel_str}")


These utility functions provide common operations that can be used throughout your CodeGenLib library and in projects that use your library. They offer a consistent way to perform file operations and string manipulations