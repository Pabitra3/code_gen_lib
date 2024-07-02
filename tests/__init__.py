import unittest
import os

def load_tests(loader, standard_tests, pattern):
    # Get the directory of this file
    this_dir = os.path.dirname(__file__)
    
    # Create a test suite
    suite = unittest.TestSuite()
    
    # Discover and load tests from all files in this directory
    for all_test_suite in unittest.defaultTestLoader.discover(start_dir=this_dir, pattern='test_*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    
    return suite

def run_all_tests():
    # Run all tests
    unittest.TextTestRunner(verbosity=2).run(load_tests(None, None, None))

if __name__ == '__main__':
    run_all_tests()