from util import sql_util, uml_util
from command import Command


def x_print(v_id, value):
    if v_id >= 0 & v_id < 10:
        a = '|  ' + str(v_id) + '   | '
    elif v_id >= 10 & v_id < 100:
        a = '|  ' + str(v_id) + '  | '
    elif v_id >= 100 & v_id < 999:
        a = '| ' + str(v_id) + '  | '
    elif v_id >= 1000 & v_id < 9999:
        a = '| ' + str(v_id) + ' | '
    else:
        a = '|' + str(v_id) + '| '
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
        if not entity == {}:
            return uml_util.draw_uml_impl(
                entity['class_name'],
                entity['field_list'],
                entity['constructor_content'],
                entity['method_list']
            )

    def usage(self):
        return "Show a UML of the given name. Pass the name as only argument."


class DeleteUMLCommand(Command):
    def check_argument(self, args):
        if not len(args) == 1:
            return False
        return True

    def execute(self, args):
        c_name=args[0]
        sql_util.delete(c_name)

    def usage(self):
        return "Show a UML of the given name. Pass the name as only argument."
