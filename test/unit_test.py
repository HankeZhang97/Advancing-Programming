import unittest
import warnings

import js_util


class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        print("Execute SetUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Execute TearDownClass")

    def setUp(self):
        print("Execute SetUp")

    def tearDown(self):
        print("Execute TearDown")

    def test_get_class_name(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        class_name = js_util.get_class_name(js_str)
        print(class_name + '\n')
        self.assertTrue('FOO'.isupper())

    def test_get_constructor_content(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        inner_str = js_util.get_class_inner_str(js_str)
        constructor_content = js_util.get_constructor_content(inner_str)
        print(constructor_content + '\n')
        self.assertTrue('FOO'.isupper())

    def test_get_field_list(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        inner_str = js_util.get_class_inner_str(js_str)
        field_list = js_util.get_field_list(inner_str)
        for item in field_list:
            print(item, end=' ')
        print('\n')
        self.assertTrue('FOO'.isupper())

    def test_get_method_list(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        inner_str = js_util.get_class_inner_str(js_str)
        method_list = js_util.get_method_list(inner_str)
        for item in method_list:
            print(item, end=' ')
        print('\n')
        self.assertTrue('FOO'.isupper())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test2("test_two"))
    suite.addTest(Test2("test_one"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
