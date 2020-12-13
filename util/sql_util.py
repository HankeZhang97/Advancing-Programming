import sqlite3


def connect():
    # conn = sqlite3.connect('../db/data.db')
    conn = sqlite3.connect('./db/data.db')
    return conn


def insert(class_name, field_list, constructor_content, method_list):
    conn = connect()
    cursor = conn.cursor()
    sql_1 = "INSERT INTO class_tb(class_name) VALUES('" + class_name + "');"
    try:
        cursor.execute(sql_1)
        sql_2 = "select * from class_tb where class_name = '" + class_name + "';"
        c = cursor.execute(sql_2)
        c.row_factory = lambda cursor, row: row[0]
        c_id = str(c.fetchone())
        if len(field_list) > 0:
            for field_item in field_list:
                cursor.execute(
                    "INSERT INTO field_tb(field_name, class_id) VALUES('" + field_item + "', " + c_id + ");"
                )
        if len(constructor_content) > 0:
            cursor.execute(
                "INSERT INTO constructor_tb(constructor_name, class_id) VALUES('" + constructor_content + "', " + c_id + ");"
            )
        if len(method_list) > 0:
            for method_item in method_list:
                cursor.execute(
                    "INSERT INTO method_tb(method_name, class_id) VALUES('" + method_item + "', " + c_id + ");"
                )
        print('Insert Successfully...')
        print(c.fetchone())
    except OSError:
        print('Insert defeated...')
    conn.commit()


def select_one(c_name):
    conn = connect()
    cursor = conn.cursor()

    entity = {}
    # class_name, field_list, constructor_content, method_list

    c = cursor.execute("select * from class_tb where class_name = '" + c_name + "'")
    c.row_factory = lambda cursor, row: {'id': row[0], 'name': row[1]}
    cla = c.fetchone()
    if cla == None:
        print('The Class does not exist...')
    else:
        entity['class_name'] = cla['name']
        c_id = str(cla['id'])

        f_c = cursor.execute("select * from field_tb where class_id = " + c_id)
        f_c.row_factory = lambda cursor, row: row[1]
        entity['field_list'] = f_c.fetchall()

        con_c = cursor.execute("select * from constructor_tb where class_id = " + c_id)
        con_c.row_factory = lambda cursor, row: row[1]
        entity['constructor_content'] = con_c.fetchone()

        m_c = cursor.execute("select * from method_tb where class_id = " + c_id)
        m_c.row_factory = lambda cursor, row: row[1]
        entity['method_list'] = m_c.fetchall()

    conn.commit()
    return entity


def select_all():
    conn = connect()
    cursor = conn.cursor()
    sql = "select * from class_tb"
    c = cursor.execute(sql)
    c.row_factory = lambda cursor, row: {'id': row[0], 'value': row[1]}
    conn.commit()
    return c.fetchall()


def delete(c_name):
    conn = connect()
    cursor = conn.cursor()
    cla_c = cursor.execute("select * from class_tb where class_name = '" + c_name + "'")
    cla_c.row_factory = lambda cursor, row: {'id': row[0], 'name': row[1]}
    cla = cla_c.fetchone()
    if not len(cla) > 0:
        print('The Class does not exist...')
    else:
        c_id = str(cla['id'])
        cursor.execute("delete from class_tb where id = " + c_id)
        cursor.execute("delete from field_tb where class_id = " + c_id)
        cursor.execute("delete from constructor_tb where class_id = " + c_id)
        cursor.execute("delete from method_tb where class_id = " + c_id)
        print('Delete Successfully...')
    conn.commit()
