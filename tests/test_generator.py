
import unittest
import os
from code_gen_lib.core.generator import CodeGenerator

class TestCodeGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = CodeGenerator('path/to/test_config.yaml')
        self.output_path = 'test_output.py'

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_generate_code(self):
        self.generator.generate_code('crud/create', self.output_path, model_name='User', fields=['id', 'name', 'email'])
        
        self.assertTrue(os.path.exists(self.output_path))
        
        with open(self.output_path, 'r') as f:
            content = f.read()
        
        self.assertIn('def create_user', content)
        self.assertIn('id', content)
        self.assertIn('name', content)
        self.assertIn('email', content)

if __name__ == '__main__':
    unittest.main()