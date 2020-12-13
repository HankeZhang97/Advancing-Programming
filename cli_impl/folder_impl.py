import os

from util.shelve_util import get_current_path, set_current_path
from pathlib import Path
from command import Command


def is_js_file(file):
    file.endswith('.js') | file.endswith('.JS') | file.endswith('.Js') | file.endswith('.jS')


class ToFolderCommand(Command):
    def check_argument(self, args):
        if len(args) != 1 or type(args[0]) != str or not args[0]:
            return False
        return True

    def execute(self, args):
        url = args[0]
        my_dir = Path(url)
        if my_dir.is_dir():
            if not url[-1:] == '\\':
                url += '\\'
            return 'Successfully...\nCurrent path: ' + set_current_path(url)
        else:
            return 'The Folder does not exist...'

    def usage(self):
        return "Change to folder command. Use folder as the only argument"


class ToDefaultFolderCommand(Command):
    def check_argument(self, args):
        if len(args) != 0:
            return False
        return True

    def execute(self, args):
        try:
            default_path = os.path.dirname(os.path.dirname(__file__)) + '\\resource\\'
            return 'Successfully...' + 'Current path: ' + set_current_path(default_path)
        except:
            return 'The Folder does not exist...'

    def usage(self):
        return "Change to folder command. Use folder as the only argument"


class ShowCurrentFolderCommand(Command):
    def check_argument(self, args):
        if len(args) != 0:
            return False
        return True

    def execute(self, args):
        return 'Current path: ' + get_current_path()

    def usage(self):
        return "Show current path command. Use no argument"


class ShowAllFilesCommand(Command):
    def check_argument(self, args):
        if len(args) != 0:
            return False
        return True

    def execute(self, args):
        files = os.listdir(get_current_path())
        return "\n".join(files)

    def usage(self):
        return "Show all files in current folder. Has no argument."


class ShowAllJSFilesCommand(Command):
    def check_argument(self, args):
        if len(args) != 0:
            return False
        return True

    def execute(self, args):
        files = os.listdir(get_current_path())
        js_files = []
        for filename in files:
            if is_js_file(filename):
                js_files.append(filename)
        return "\n".join(js_files)

    def usage(self):
        return "Show all js files in current folder. Has no argument."
