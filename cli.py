from cmdtree import INT, entry, command, argument, option, group
from cli_impl import db_impl, folder_impl, js_impl


@argument("host", help="server listen address")
@option("reload", is_flag=True, help="if auto-reload on")
@option("port", help="server port", type=INT, default=8888)
@command(name='don', help="run a http server on given address")
def run_server(host, reload, port):
    print(
        "Your server running on {host}:{port}, auto-reload is {reload}".format(
            host=host,
            port=port,
            reload=reload
        )
    )


# -------------------- folder -------------------- #
# ok
@group("folder")
@command(name='folder', help="run the uml operate")
def folder():
    pass


# ok
@folder.command(name='to', help='Open the folder.(Need Parameter - The Folder URL)')
@argument(name='url', help='The Folder URL.')
def to(url):
    print('------------------------------')
    folder_impl.to_folder(url)


# ok
@folder.command(name='default', help='Show the Default Folder.')
def to_default():
    print('------------------------------')
    folder_impl.to_default_folder()


# ok
@folder.command(name='current', help='Show the Current Folder.')
def current():
    print('------------------------------')
    folder_impl.current_folder()


# ok
@folder.command(name='ls', help='Show all files in the folder')
def ls():
    print('------------------------------')
    folder_impl.show_all_file()


# ok
@folder.command(name='lsjs', help='Only display .js files in the folder')
def lsjs():
    print('------------------------------')
    folder_impl.show_all_js()


# -------------------- js -------------------- #
# ok
@group("showcode")
@command(name='showcode', help='Display the content code of the .js file.(Need Parameter - the .js file name)')
@argument(name='js_name', help='The .js file name')
def showcode(js_name):
    js_impl.show_js_code(js_name)


# ok
@group("showuml")
@command(name='showuml', help='Display the UML structure diagram of the .js file.(Need Parameter - the .js file '
                              'name)')
@argument("js_name")
def showuml(js_name):
    print('------------------------------')
    js_impl.show_js_uml(js_name)


@group("saveuml")
@command(name='saveuml', help='Save the uml structure diagram to the sqlite database.(Need Parameter - the .js '
                              'file name)')
@argument("js_name")
def saveuml(js_name):
    print('------------------------------')
    js_impl.save_js_uml(js_name)


# -------------------- db -------------------- #
@group("db")
@command(name='db', help="run database operate")
def db():
    pass


@db.command(name='list', help='Display a list of all saved uml structure diagrams')
def list():
    print('------------------------------')
    print('All UML in the database')
    db_impl.list_all_uml()


@db.command(name='show', help='Saved uml structure diagram showing characteristics')
@argument("c_name")
def show(c_name):
    print('------------------------------')
    db_impl.show_uml(c_name)


@db.command(name='delete', help='Delete the saved uml structure diagram of the characteristic')
@argument("c_name")
def delete(c_name):
    print('------------------------------')
    db_impl.delete_uml(c_name)


if __name__ == "__main__":
    entry()
