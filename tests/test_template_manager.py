import unittest
import os
import tempfile
from code_gen_lib.core.template_manager import TemplateManager

class TestTemplateManager(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for test templates
        self.temp_dir = tempfile.mkdtemp()
        
        # Create some test template files
        self.create_test_template('test1.py', 'Content of test1')
        self.create_test_template('test2.py', 'Content of test2')
        self.create_test_template('not_a_template.txt', 'This should not be listed')

        # Initialize TemplateManager with the temp directory
        self.template_manager = TemplateManager(self.temp_dir)

    def tearDown(self):
        # Clean up the temporary directory
        for filename in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, filename))
        os.rmdir(self.temp_dir)

    def create_test_template(self, filename, content):
        with open(os.path.join(self.temp_dir, filename), 'w') as f:
            f.write(content)

    def test_list_templates(self):
        templates = self.template_manager.list_templates()
        self.assertEqual(len(templates), 2)
        self.assertIn('test1.py', templates)
        self.assertIn('test2.py', templates)
        self.assertNotIn('not_a_template.txt', templates)

    def test_get_template_content(self):
        content = self.template_manager.get_template_content('test1')
        self.assertEqual(content, 'Content of test1')

    def test_get_template_content_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            self.template_manager.get_template_content('nonexistent')

    def test_template_dir_not_found(self):
        with self.assertRaises(FileNotFoundError):
            TemplateManager('nonexistent_dir')

    def test_empty_template_dir(self):
        empty_dir = tempfile.mkdtemp()
        tm = TemplateManager(empty_dir)
        self.assertEqual(tm.list_templates(), [])
        os.rmdir(empty_dir)

    def test_list_templates_with_subdirectories(self):
        subdir = os.path.join(self.temp_dir, 'subdir')
        os.mkdir(subdir)
        self.create_test_template(os.path.join('subdir', 'test3.py'), 'Content of test3')
        templates = self.template_manager.list_templates()
        self.assertEqual(len(templates), 2)  # Should still only list top-level .py files
        self.assertNotIn('test3.py', templates)

    def test_get_template_content_with_extension(self):
        content = self.template_manager.get_template_content('test2.py')
        self.assertEqual(content, 'Content of test2')

if __name__ == '__main__':
    unittest.main()