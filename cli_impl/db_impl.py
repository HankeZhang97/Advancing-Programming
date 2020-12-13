from util import sql_util, uml_util


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
    print(a + value)


def list_all_uml():
    c_list = sql_util.select_all()
    print('|  ID  | Class Name')
    for item in c_list:
        x_print(item['id'], item['value'])


def show_uml(c_name):
    entity = sql_util.select_one(c_name)
    if not entity == {}:
        uml_util.draw_uml_impl(
            entity['class_name'],
            entity['field_list'],
            entity['constructor_content'],
            entity['method_list'])


def delete_uml(c_name):
    sql_util.delete(c_name)
    list_all_uml()