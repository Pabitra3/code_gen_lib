# ConfigManager API Reference

The `ConfigManager` class is responsible for managing configuration settings in the CodeGenLib library. It provides methods for loading, accessing, modifying, and saving configuration data.

## Table of Contents

1. [Class Definition](#class-definition)
2. [Methods](#methods)
   - [__init__](#__init__)
   - [load_config](#load_config)
   - [get_config_value](#get_config_value)
   - [set_config_value](#set_config_value)
   - [save_config](#save_config)
3. [Exceptions](#exceptions)
4. [Usage Examples](#usage-examples)

## Class Definition

```python
class ConfigManager:
    """
    Manages configuration settings for code generation.
    """



Methods
init
def __init__(self, config_file: str):
    """
    Initialize the ConfigManager.

    Args:
        config_file (str): Path to the configuration file.
    """
Initializes a new instance of the ConfigManager class.
Parameters:

config_file (str): Path to the configuration file.

Raises:

FileNotFoundError: If the specified configuration file does not exist.


load_config
def load_config(self) -> Dict[str, Any]:
    """
    Load the configuration from the file.

    Returns:
        Dict[str, Any]: The loaded configuration as a dictionary.

    Raises:
        ConfigurationError: If there's an error parsing the configuration file.
    """
Loads the configuration from the file.
Returns:

Dict[str, Any]: The loaded configuration as a dictionary.

Raises:

ConfigurationError: If there's an error parsing the configuration file.


get_config_value
def get_config_value(self, key: str) -> Any:
    """
    Get a configuration value.

    Args:
        key (str): The configuration key, can use dot notation for nested keys.

    Returns:
        Any: The configuration value.

    Raises:
        KeyError: If the specified key is not found in the configuration.
    """
Retrieves a configuration value.
Parameters:

key (str): The configuration key, can use dot notation for nested keys.

Returns:

Any: The configuration value.

Raises:

KeyError: If the specified key is not found in the configuration.


set_config_value
def set_config_value(self, key: str, value: Any) -> None:
    """
    Set a configuration value.

    Args:
        key (str): The configuration key, can use dot notation for nested keys.
        value (Any): The value to set.
    """
Sets a configuration value.
Parameters:

key (str): The configuration key, can use dot notation for nested keys.
value (Any): The value to set.


save_config
def save_config(self) -> None:
    """
    Save the current configuration to the file.

    Raises:
        IOError: If there's an error writing to the configuration file.
    """
Saves the current configuration to the file.
Raises:

IOError: If there's an error writing to the configuration file.

Exceptions

ConfigurationError: Raised when there's an error parsing the configuration file.
KeyError: Raised when a specified configuration key is not found.
IOError: Raised when there's an error writing to the configuration file.
FileNotFoundError: Raised when the specified configuration file does not exist.

Usage Examples
Initializing ConfigManager
from code_gen_lib.core import ConfigManager

config_manager = ConfigManager('config.yaml')

Loading Configuration
try:
    config = config_manager.load_config()
    print(f"Loaded configuration: {config}")
except ConfigurationError as e:
    print(f"Error loading configuration: {e}")


Getting Configuration Values
try:
    db_host = config_manager.get_config_value('database.host')
    print(f"Database host: {db_host}")
except KeyError as e:
    print(f"Configuration key not found: {e}")


Setting Configuration Values
config_manager.set_config_value('database.port', 5432)
print("Database port updated")

Saving Configuration
try:
    config_manager.save_config()
    print("Configuration saved successfully")
except IOError as e:
    print(f"Error saving configuration: {e}")

Handling Nested Configuration
# Accessing nested configuration
try:
    log_level = config_manager.get_config_value('logging.level')
    print(f"Log level: {log_level}")
except KeyError as e:
    print(f"Configuration key not found: {e}")

# Setting nested configuration
config_manager.set_config_value('logging.file.path', '/var/log/codegen.log')
print("Log file path updated")


This API reference provides developers with a comprehensive guide to using the ConfigManager class in your CodeGenLib library. It includes detailed information about each method, including parameters, return values, and potential exceptions. The usage examples demonstrate how to use each method in practice, including handling of nested configuration keys.