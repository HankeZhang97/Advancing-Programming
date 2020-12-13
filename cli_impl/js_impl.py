from util import uml_util, js_util
from util.shelve_util import get_current_path


def set_js_name(name):
    if not name.endswith('.js') | name.endswith('.JS') | name.endswith('.Js') | name.endswith('.jS'):
        return name + '.js'
    return name


def show_js_code(js_name):
    js_str = js_util.get_js_str(get_current_path(), set_js_name(js_name))
    print('-------------------- START --------------------\n')
    print(js_str)
    print('\n-------------------- END --------------------')


def show_js_uml(js_name):
    uml_util.draw_uml(get_current_path(), set_js_name(js_name))


def save_js_uml(js_name):
    uml_util.save_uml(get_current_path(), set_js_name(js_name))
    print("The UML of '" + set_js_name(js_name) + "' Save successfully...")