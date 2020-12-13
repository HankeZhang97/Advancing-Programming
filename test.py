import unittest
import warnings

from util import js_util
from command import commandInvoker
from doctest import testmod

from util import js_util

js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
js_name = 'employee.js'


class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        print("Execute SetUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Execute TearDownClass")

    def setUp(self):
        self.commandInvoker = commandInvoker
        self.commandInvoker.execute("delete_uml Boss")
        print("Execute SetUp")

    def tearDown(self):
        print("Execute TearDown")

    def test_get_class_name(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        class_name = js_util.get_class_name(js_str)
        print(class_name + '\n')
        self.assertTrue('FOO'.isupper())

    def test_get_constructor_content(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        inner_str = js_util.get_class_inner_str(js_str)
        constructor_content = js_util.get_constructor_content(inner_str)
        print(constructor_content + '\n')
        self.assertTrue('FOO'.isupper())

    def test_get_field_list(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        inner_str = js_util.get_class_inner_str(js_str)
        field_list = js_util.get_field_list(inner_str)
        for item in field_list:
            print(item, end=' ')
        print('\n')
        self.assertTrue('FOO'.isupper())

    def test_get_method_list(self):
        js_path = 'C:\\Users\\Donecro\\Project\\Py Cli\\code_cli\\resource\\'
        js_name = 'employee.js'
        js_str = js_util.get_js_str(js_path, js_name)
        inner_str = js_util.get_class_inner_str(js_str)
        method_list = js_util.get_method_list(inner_str)
        for item in method_list:
            print(item, end=' ')
        print('\n')
        self.assertTrue('FOO'.isupper())

    def test_bad_argument(self):
        r = self.commandInvoker.execute("no_such_command")
        self.assertEqual(r, "No such command. Registered commands are dict_keys(['current_folder', 'list_js_files', "
                            "'list_files', 'to_default', 'to_folder', 'save_js_uml', 'show_js_uml', 'show_js_code', "
                            "'show_uml', 'list_uml', 'delete_uml'])")

        r = self.commandInvoker.execute("current_folder bad_argument")
        self.assertEqual(r, "Show current path command. Use no argument")

        r = self.commandInvoker.execute("list_js_files bad_argument")
        self.assertEqual(r, "Show all js files in current folder. Has no argument.")

        r = self.commandInvoker.execute("list_files bad_argument")
        self.assertEqual(r, "Show all files in current folder. Has no argument.")

        r = self.commandInvoker.execute("to_default bad_argument")
        self.assertEqual(r, "Change to folder command. Use no argument")

        r = self.commandInvoker.execute("to_folder")
        self.assertEqual(r, "Change to folder command. Use folder as the only argument")

        r = self.commandInvoker.execute("to_folder no_such_folder")
        self.assertEqual(r, 'The Folder does not exist...')

        r = self.commandInvoker.execute("save_js_uml")
        self.assertEqual(r, "Save JS UML command. Pass filename as the only argument")

        r = self.commandInvoker.execute("show_js_uml")
        self.assertEqual(r, "Show JS UML command. Pass filename as the only argument")

        r = self.commandInvoker.execute("show_js_code")
        self.assertEqual(r, "Show JS code command. Pass filename as the only argument")

        r = self.commandInvoker.execute("show_uml")
        self.assertEqual(r, "Show a UML of the given name. Pass the name as only argument.")

        r = self.commandInvoker.execute("list_uml bad_argument")
        self.assertEqual(r, "List all uml command. Pass no argument.")

        r = self.commandInvoker.execute("delete_uml")
        self.assertEqual(r, "Delete a UML of the given name. Pass the name as only argument.")

    def test_normal_execute(self):
        r = self.commandInvoker.execute("current_folder")
        self.assertEqual(r, "Current path: C:\\Users\\yh\\PycharmProjects\\FinalProject\\resource\\")

        r = self.commandInvoker.execute("list_js_files")
        self.assertEqual(r, "boss.js\nemployee.js\nmanager.js")

        r = self.commandInvoker.execute("list_files")
        self.assertEqual(r, "boss.js\nemployee.js\nhaha.txt\nmanager.js")

        r = self.commandInvoker.execute("to_default")
        self.assertEqual(r, "Current path: C:\\Users\\yh\\PycharmProjects\\FinalProject\\resource\\")

        r = self.commandInvoker.execute("to_folder db")
        self.assertEqual(r, "Current path: db\\")

        self.commandInvoker.execute("to_default")

        r = self.commandInvoker.execute("save_js_uml boss.js")
        self.assertEqual(r, "The UML of 'boss.js' Save successfully...")

        r = self.commandInvoker.execute("save_js_uml no_such_file")
        self.assertEqual(r, "Save failed")

        r = self.commandInvoker.execute("show_js_uml boss.js")

        expected = "------------------------------\n" \
                   "| - Boss: class              |\n" \
                   "|----------------------------|\n" \
                   "| - name: object             |\n" \
                   "| - age: object              |\n" \
                   "| - gender: object           |\n" \
                   "| - skill: object            |\n" \
                   "| - hobby: object            |\n" \
                   "| - salary: object           |\n" \
                   "|----------------------------|\n" \
                   "| - constructor(name, age, g |\n" \
                   "| ender, skill, hobby, salar |\n" \
                   "| y)                         |\n" \
                   "| - test01(item): void       |\n" \
                   "| - test_02(item, index): vo |\n" \
                   "| id                         |\n" \
                   "| - test03(ok): void         |\n" \
                   "| - test04(ok, q): void      |\n" \
                   "| - test05(): void           |\n" \
                   "| - test06(): void           |\n" \
                   "------------------------------\n"
        self.assertEqual(r, expected)

        r = self.commandInvoker.execute("show_js_code boss.js")
        expected = """-------------------- START --------------------

class Boss extends Manager {
    constructor(name, age, gender, skill, hobby, salary){
        super(name, age, gender, skill)
        this.hobby = hobby
        this.salary = salary
    }

    de = {'a': 3}
      test01 ( item )   {
        console.log("The boss...")
    }

    test_02 ( item, index )   {
        console.log("The boss...")
    }

    test03 (ok)   {
        console.log("The boss...")
    }

    test04 (ok,q)   {
        console.log("The boss...")
    }

    test05 ()   {
        console.log("The boss...")
    }

    test06  ()   {
        console.log("The boss...")
    }
}

const boss = new Boss(
    "don",
    {a: 18 },
    "male",
    ["es6","vue","react"],
    "study",
    "10k"
)

console.log(boss)

boss.desc()

boss.say()
-------------------- END --------------------"""
        expected = "\n".join(expected.split("\n"))
        self.assertEqual(r, expected)

        r = self.commandInvoker.execute("show_uml Boss")
        expected = """------------------------------
| - Boss: class              |
|----------------------------|
| - name: object             |
| - age: object              |
| - gender: object           |
| - skill: object            |
| - hobby: object            |
| - salary: object           |
|----------------------------|
| - constructor(name, age, g |
| ender, skill, hobby, salar |
| y)                         |
| - test01(item): void       |
| - test_02(item, index): vo |
| id                         |
| - test03(ok): void         |
| - test04(ok, q): void      |
| - test05(): void           |
| - test06(): void           |
------------------------------
"""
        self.assertEqual(r, expected)

        r = self.commandInvoker.execute("list_uml")
        self.assertTrue("Boss" in r)

        r = self.commandInvoker.execute("delete_uml Boss")
        self.assertEqual(r, "Delete Successfully")

        r = self.commandInvoker.execute("delete_uml Boss")
        self.assertEqual(r, "Delete Failed")

def test_get_class_name(c_path, c_name):
    """
    >>> test_get_class_name(js_path, js_name)
    'Employee'
    """
    js_str = js_util.get_js_str(c_path, c_name)
    class_name = js_util.get_class_name(js_str)
    return class_name


def test_get_constructor_content(c_path, c_name):
    """
    >>> test_get_constructor_content(js_path, js_name)
    'constructor(name, age, gender)'
    """
    js_str = js_util.get_js_str(c_path, c_name)
    inner_str = js_util.get_class_inner_str(js_str)
    constructor_content = js_util.get_constructor_content(inner_str)
    return constructor_content


def test_get_field_list(c_path, c_name):
    """
    >>> test_get_field_list(js_path, js_name)
    ['name', 'age', 'gender']
    """
    js_str = js_util.get_js_str(c_path, c_name)
    inner_str = js_util.get_class_inner_str(js_str)
    field_list = js_util.get_field_list(inner_str)
    return field_list


def test_get_method_list(c_path, c_name):
    """
    >>> test_get_method_list(js_path, js_name)
    ['desc()', 'call()']
    """
    js_str = js_util.get_js_str(c_path, c_name)
    inner_str = js_util.get_class_inner_str(js_str)
    method_list = js_util.get_method_list(inner_str)
    return method_list


if __name__ == "__main__":
    unittest.main()
    testmod(verbose=True)
