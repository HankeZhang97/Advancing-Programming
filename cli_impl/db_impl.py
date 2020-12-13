from util import sql_util, uml_util
from command import Command
from collections import defaultdict
import math


def x_print(v_id, value):
    format_map = defaultdict(lambda: '|%s| ')
    format_map.update({
        0: '|  %s   | ',
        1: '|  %s  | ',
        2: '| %s  | ',
        3: '| %s | ',
    })
    a = format_map[int(math.log(v_id))]
    return a + value + "\n"


class ListAllUMLCommand(Command):
    def check_argument(self, args):
        if not len(args) == 0:
            return False
        return True

    def execute(self, args):
        result = "|  ID  | Class Name\n"
        c_list = sql_util.select_all()
        for item in c_list:
            result += x_print(item['id'], item['value'])
        return result

    def usage(self):
        return "List all uml command. Pass no argument."


class ShowUMLCommand(Command):
    def check_argument(self, args):
        if not len(args) == 1:
            return False
        return True

    def execute(self, args):
        c_name=args[0]
        entity = sql_util.select_one(c_name)
        if entity:
            return uml_util.draw_uml_impl(
                entity['class_name'],
                entity['field_list'],
                entity['constructor_content'],
                entity['method_list']
            )
        return "No such entity"

    def usage(self):
        return "Show a UML of the given name. Pass the name as only argument."


class DeleteUMLCommand(Command):
    def check_argument(self, args):
        if not len(args) == 1:
            return False
        return True

    def execute(self, args):
        c_name = args[0]
        if sql_util.delete(c_name):
            return "Delete Successfully"
        else:
            return "Delete Failed"

    def usage(self):
        return "Delete a UML of the given name. Pass the name as only argument."
