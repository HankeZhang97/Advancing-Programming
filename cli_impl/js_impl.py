from command import Command
from util import uml_util, js_util
from util.shelve_util import get_current_path


def set_js_name(name):
    if not name.endswith('.js') | name.endswith('.JS') | name.endswith('.Js') | name.endswith('.jS'):
        return name + '.js'
    return name


class ShowJSCodeCommand(Command):
    def check_argument(self, args):
        if len(args) != 1:
            return False
        return True

    def execute(self, args):
        js_str = js_util.get_js_str(get_current_path(), set_js_name(args[0]))
        return "-------------------- START --------------------\n" + js_str +\
               '\n-------------------- END --------------------'

    def usage(self):
        return "Show JS code command. Pass filename as the only argument"


class ShowJSUMLCommand(Command):
    def check_argument(self, args):
        if len(args) != 1:
            return False
        return True

    def execute(self, args):
        return uml_util.draw_uml(get_current_path(), set_js_name(args[0]))

    def usage(self):
        return "Show JS code command. Pass filename as the only argument"


class SaveJSUMLCommand(Command):
    def check_argument(self, args):
        if len(args) != 1:
            return False
        return True

    def execute(self, args):
        uml_util.save_uml(get_current_path(), set_js_name(args[0]))
        return "The UML of '" + set_js_name(args[0]) + "' Save successfully..."

    def usage(self):
        return "Save JS code command. Pass filename as the only argument"
