from doctest import testmod

import js_util

js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
js_name = 'employee.js'


def test_get_class_name(c_path, c_name):
    """
    >>> test_get_class_name(js_path, js_name)
    'Employee'
    """
    js_str = js_util.get_js_str(c_path, c_name)
    class_name = js_util.get_class_name(js_str)
    return class_name


def test_get_constructor_content(c_path, c_name):
    """
    >>> test_get_constructor_content(js_path, js_name)
    'constructor(name, age, gender)'
    """
    js_str = js_util.get_js_str(c_path, c_name)
    inner_str = js_util.get_class_inner_str(js_str)
    constructor_content = js_util.get_constructor_content(inner_str)
    return constructor_content


def test_get_field_list(c_path, c_name):
    """
    >>> test_get_field_list(js_path, js_name)
    ['name', 'age', 'gender']
    """
    js_str = js_util.get_js_str(c_path, c_name)
    inner_str = js_util.get_class_inner_str(js_str)
    field_list = js_util.get_field_list(inner_str)
    return field_list


def test_get_method_list(c_path, c_name):
    """
    >>> test_get_method_list(js_path, js_name)
    ['desc()', 'call()']
    """
    js_str = js_util.get_js_str(c_path, c_name)
    inner_str = js_util.get_class_inner_str(js_str)
    method_list = js_util.get_method_list(inner_str)
    return method_list


if __name__ == '__main__':
    testmod(verbose=True)
