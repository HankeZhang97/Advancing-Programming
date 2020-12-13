import time


class Command(object):
    def check_argument(self, args):
        pass

    def execute(self, args):
        pass

    def usage(self):
        pass


class CommandInvoker(object):
    def __init__(self):
        self._commands = {}
        self._history = []

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command):
        command_name, *args = command.strip().split(" ")
        if command_name not in self._commands:
            return "No such command. Registered commands are " + str(self._commands.keys())
        command_object = self._commands[command_name]
        if not command_object.check_argument(args):
            return command_object.usage()
        self._history.append((time.time(), command_name))
        return command_object.execute(args)

from cli_impl.folder_impl import ShowAllFilesCommand, ShowAllJSFilesCommand, ShowCurrentFolderCommand, \
    ToDefaultFolderCommand, ToFolderCommand

commandInvoker = CommandInvoker()
commandInvoker.register("current_folder", ShowCurrentFolderCommand())
commandInvoker.register("list_js_files", ShowAllJSFilesCommand())
commandInvoker.register("list_files", ShowAllFilesCommand())
commandInvoker.register("to_default", ToDefaultFolderCommand())
commandInvoker.register("to_folder", ToFolderCommand())

from cli_impl.js_impl import SaveJSUMLCommand, ShowJSCodeCommand, ShowJSUMLCommand

commandInvoker.register("save_js_uml", SaveJSUMLCommand())
commandInvoker.register("show_js_uml", ShowJSUMLCommand())
commandInvoker.register("show_js_code", ShowJSCodeCommand())

from cli_impl.db_impl import ShowUMLCommand, ListAllUMLCommand, DeleteUMLCommand

commandInvoker.register("show_uml", ShowUMLCommand())
commandInvoker.register("list_uml", ListAllUMLCommand())
commandInvoker.register("delete_uml", DeleteUMLCommand())
