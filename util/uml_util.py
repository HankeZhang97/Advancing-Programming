from util.sql_util import insert
from util.js_util import *

# Class
# Field
# Constructor 11
# Method


def save_uml(path, js_name):
    js_str = get_js_str(path, js_name)
    # Class
    class_name = get_class_name(js_str)

    inner_str = get_class_inner_str(js_str)

    # Field_list
    field_list = get_field_list(inner_str)

    # Constructor
    constructor_content = get_constructor_content(inner_str)

    # Method_list
    method_list = get_method_list(inner_str)

    insert(class_name, field_list, constructor_content, method_list)


def draw_uml(path, js_name):
    js_str = get_js_str(path, js_name)

    inner_str = get_class_inner_str(js_str)

    # Class
    class_name = get_class_name(js_str)

    # Field_list
    field_list = get_field_list(inner_str)

    # Constructor
    constructor_content = get_constructor_content(inner_str)

    # Method_list
    method_list = get_method_list(inner_str)

    return draw_uml_impl(class_name, field_list, constructor_content, method_list)


def draw_uml_impl(class_name, field_list, constructor_content, method_list):
    result = '------------------------------\n'
    result += ex_print(class_name + ': class')
    result += '|----------------------------|\n'
    for field_item in field_list:
        result += ex_print(field_item + ': object')
    result += '|----------------------------|\n'
    result += ex_print(constructor_content)
    for method_item in method_list:
        result += ex_print(method_item + ': void')
    result += '------------------------------\n'
    return result
