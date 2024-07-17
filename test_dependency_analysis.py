import unittest
from Dependency_Analysis import parse_nicad_xml, analyze_dependencies

class TestDependencyAnalysis(unittest.TestCase):

    def setUp(self):
        self.base_path = '/path/to/base'
        self.project_path = '/path/to/project'

    def test_no_dependencies(self):
        code = '''
def foo():
    return 42
'''
        clone_pair = [('file1.py', 1, 3)]
        has_deps, reason = analyze_dependencies(clone_pair, self.base_path, self.project_path)
        self.assertFalse(has_deps)
        self.assertEqual(reason, "")

    def test_class_dependencies(self):
        code = '''
class MyClass:
    def method(self):
        self.attribute = 42
'''
        clone_pair = [('file2.py', 1, 5)]
        has_deps, reason = analyze_dependencies(clone_pair, self.base_path, self.project_path)
        self.assertTrue(has_deps)
        self.assertIn("Class dependency", reason)

    def test_self_in_methods(self):
        code = '''
class AnotherClass:
    def another_method(self):
        self.another_attribute = 42
'''
        clone_pair = [('file3.py', 1, 5)]
        has_deps, reason = analyze_dependencies(clone_pair, self.base_path, self.project_path)
        self.assertTrue(has_deps)
        self.assertIn("Method another_method with 'self'", reason)

    def test_syntax_error(self):
        code = '''
def invalid_code(
    return 42
'''
        clone_pair = [('file4.py', 1, 3)]
        has_deps, reason = analyze_dependencies(clone_pair, self.base_path, self.project_path)
        self.assertTrue(has_deps)
        self.assertIn("Syntax error", reason)

if __name__ == '__main__':
    unittest.main()
