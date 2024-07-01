import os
import shutil
import json
import yaml

def ensure_directory(directory):
    """
    Ensure that a directory exists, creating it if necessary.

    Args:
        directory (str): The path to the directory.

    Raises:
        OSError: If the directory cannot be created.
    """
    os.makedirs(directory, exist_ok=True)

def write_file(file_path, content, mode='w'):
    """
    Write content to a file.

    Args:
        file_path (str): The path to the file.
        content (str): The content to write.
        mode (str): The mode to open the file in. Defaults to 'w' (write).

    Raises:
        IOError: If the file cannot be written to.
    """
    ensure_directory(os.path.dirname(file_path))
    with open(file_path, mode) as f:
        f.write(content)

def read_file(file_path, mode='r'):
    """
    Read content from a file.

    Args:
        file_path (str): The path to the file.
        mode (str): The mode to open the file in. Defaults to 'r' (read).

    Returns:
        str: The content of the file.

    Raises:
        IOError: If the file cannot be read.
    """
    with open(file_path, mode) as f:
        return f.read()

def copy_file(src, dst):
    """
    Copy a file from source to destination.

    Args:
        src (str): The path to the source file.
        dst (str): The path to the destination file.

    Raises:
        IOError: If the file cannot be copied.
    """
    shutil.copy2(src, dst)

def move_file(src, dst):
    """
    Move a file from source to destination.

    Args:
        src (str): The path to the source file.
        dst (str): The path to the destination file.

    Raises:
        IOError: If the file cannot be moved.
    """
    shutil.move(src, dst)

def delete_file(file_path):
    """
    Delete a file.

    Args:
        file_path (str): The path to the file to delete.

    Raises:
        IOError: If the file cannot be deleted.
    """
    os.remove(file_path)

def list_files(directory, extension=None):
    """
    List all files in a directory, optionally filtered by extension.

    Args:
        directory (str): The path to the directory.
        extension (str, optional): The file extension to filter by.

    Returns:
        list: A list of file names in the directory.

    Raises:
        OSError: If the directory cannot be read.
    """
    files = os.listdir(directory)
    if extension:
        return [f for f in files if f.endswith(extension)]
    return files

def read_json(file_path):
    """
    Read a JSON file and return its contents as a Python object.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file as a Python object.

    Raises:
        IOError: If the file cannot be read.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json(file_path, data, indent=4):
    """
    Write a Python object to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The Python object to write.
        indent (int): The indentation level for the JSON file. Defaults to 4.

    Raises:
        IOError: If the file cannot be written to.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=indent)

def read_yaml(file_path):
    """
    Read a YAML file and return its contents as a Python object.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a Python object.

    Raises:
        IOError: If the file cannot be read.
        yaml.YAMLError: If the file is not valid YAML.
    """
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def write_yaml(file_path, data):
    """
    Write a Python object to a YAML file.

    Args:
        file_path (str): The path to the YAML file.
        data (dict): The Python object to write.

    Raises:
        IOError: If the file cannot be written to.
    """
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def get_file_size(file_path):
    """
    Get the size of a file in bytes.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The size of the file in bytes.

    Raises:
        OSError: If the file cannot be accessed.
    """
    return os.path.getsize(file_path)

def get_file_modification_time(file_path):
    """
    Get the last modification time of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        float: The last modification time of the file (in seconds since the epoch).

    Raises:
        OSError: If the file cannot be accessed.
    """
    return os.path.getmtime(file_path)
