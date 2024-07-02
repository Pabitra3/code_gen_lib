import unittest
import os
import tempfile
import yaml
from code_gen_lib.core.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for test configs
        self.temp_dir = tempfile.mkdtemp()
        
        # Create a test config file
        self.config_data = {
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'testdb'
            },
            'templates': {
                'path': '/path/to/templates'
            },
            'output': {
                'directory': '/path/to/output'
            }
        }
        self.config_file = os.path.join(self.temp_dir, 'test_config.yaml')
        with open(self.config_file, 'w') as f:
            yaml.dump(self.config_data, f)

        # Initialize ConfigManager with the temp config file
        self.config_manager = ConfigManager(self.config_file)

    def tearDown(self):
        # Clean up the temporary directory
        os.remove(self.config_file)
        os.rmdir(self.temp_dir)

    def test_load_config(self):
        config = self.config_manager.load_config()
        self.assertEqual(config, self.config_data)

    def test_get_config_value(self):
        self.assertEqual(self.config_manager.get_config_value('database.host'), 'localhost')
        self.assertEqual(self.config_manager.get_config_value('database.port'), 5432)
        self.assertEqual(self.config_manager.get_config_value('templates.path'), '/path/to/templates')

    def test_get_config_value_nested(self):
        self.assertEqual(self.config_manager.get_config_value('database'), self.config_data['database'])

    def test_get_config_value_nonexistent(self):
        with self.assertRaises(KeyError):
            self.config_manager.get_config_value('nonexistent.key')

    def test_set_config_value(self):
        self.config_manager.set_config_value('database.host', '127.0.0.1')
        self.assertEqual(self.config_manager.get_config_value('database.host'), '127.0.0.1')

    def test_set_config_value_new_key(self):
        self.config_manager.set_config_value('new.key', 'new_value')
        self.assertEqual(self.config_manager.get_config_value('new.key'), 'new_value')

    def test_save_config(self):
        self.config_manager.set_config_value('database.host', '127.0.0.1')
        self.config_manager.save_config()

        # Load the config file again to check if changes were saved
        with open(self.config_file, 'r') as f:
            saved_config = yaml.safe_load(f)

        self.assertEqual(saved_config['database']['host'], '127.0.0.1')

    def test_config_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            ConfigManager('nonexistent_config.yaml')

    def test_invalid_yaml(self):
        invalid_config_file = os.path.join(self.temp_dir, 'invalid_config.yaml')
        with open(invalid_config_file, 'w') as f:
            f.write('invalid: yaml: content')

        with self.assertRaises(yaml.YAMLError):
            ConfigManager(invalid_config_file)

        os.remove(invalid_config_file)

if __name__ == '__main__':
    unittest.main()