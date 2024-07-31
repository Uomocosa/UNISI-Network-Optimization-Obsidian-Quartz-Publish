###### How to make it work
1. Find your ***Sublime Text/User Folder***, it should be somenthing like:<br>`C:\Users\Uomocosa\AppData\Roaming\Sublime Text\Packages\User`.
2. Create two new files:
	- `myPython.sublime-build` 
	- `myPython.py` 
3. In any another folder in your pc, create a new folder then in it create a new python file.
4. Open the new python file in Sublime Text.
5. Write the code and build it like normal.<br>==***NOTE***: If you open the file and build it really fast, it will be slow==.<br>***NOTE***: This will create a new custom `__init__.py` file to allow for simple relative imports inside of this package.<br>==If you do not want any, or wish to have another handmade  `__init__.py` file in this folder, you just need to create a new text file callled `__do_not_create_a_venv_here__.txt` inside this folder==.<br>***NOTE***: This will create a new [[Sublime Text - pipenv|pipenv venv (virtual environment)]].<br>==If you do not want it, you just need to create a new text file callled `.txt` inside this folder==.
---
###### myPython.sublime-build
```json
{
    "target": "my_python", //Refering to: myPythonCommand
    "selector": "source.python",
    "cmd": ["py", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "env": {"PYTHONIOENCODING": "utf-8"},
    "encoding": "utf-8"
}
```

---
###### myPython.py
```python
import sublime
import sublime_plugin
import subprocess
import os
from pathlib import Path
import pickle 
# import asyncio
from time import time
from collections.abc import Iterable
import shutil



DEBUG = False
def D(debug_message, *args, **kwargs): 
    if DEBUG: print(">>> "+debug_message, *args, **kwargs) 

VENV_NOT_ALLOWED_FILE_NAMES = (
    "__do_not_create_a_venv_here__.txt",
    ".no_venv.txt",
)

ALREADY_COPIED = False
FILES_TO_COPY = [
    {
        'file_name_to_copy':    "__TO_BE_COPIED__ [__init__].py",
        'new_name':             "__init__.py",
        'except_if_in_folder_there_is': "__do_not_create_the_custom__init__here__.txt",
    },
    {
        'file_name_to_copy':    "__TO_BE_COPIED__ [(pipenv) README].txt",
        'new_name':             "(pipenv) README.txt",
        'except_if_in_folder_there_is': "__do_not_create_a_venv_here__.txt",
    },
]


FILE2INTERPRETER_DICT = None

# POSSIBLE PROBLEMS and or future upgrades:
#   The file related to FILE2INTERPRETER_DICT, may become too big,
#       so loading and saving may become a problem, to solve this a method
#       to reduce its size, may be deleting old entries, or creating a smarter
#       function, like one that finds the '.pipfile' and saves only that folder as key,
#       all other subfolder, are not saved.

class myPythonCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        D("myPythonCommand")
        kwargs = handle_pipenv_venv(**kwargs)
        copy_useful_files_in_folder(**kwargs)
        self.window.run_command("exec", kwargs)


class myPythonEventListener(sublime_plugin.EventListener):
    def on_load_async(self, view):
        D("on_load_async")
        self.create_venv_and_useful_files(view)

    def on_new_async(self, view):
        D("on_new_async")
        self.create_venv_and_useful_files(view)

    def on_post_save_async(self, view):
        D("on_save_async")
        self.create_venv_and_useful_files(view)

    def create_venv_and_useful_files(self, view):
        file_Path = Path(view.file_name()).absolute()
        D(f"file_Path:\n\t{file_Path}")
        if can_a_venv_be_created_here(file_Path):
            find_or_create_python_interpreter(file_Path = file_Path)
        copy_useful_files_in_folder(file_Path)



def get_file_path_form_kwargs(**kwargs):
    return kwargs['cmd'][2]

def get_User_folder_Path():
    return Path(sublime.packages_path()).absolute() / "User"

def copy_folder_or_file(source_path, destination_path):
    if os.path.isdir(source_path):
        shutil.copytree(source_path, destination_path)
    if os.path.isfile(source_path):
        shutil.copyfile(source_path, destination_path)

def copy_useful_files_in_folder(file_Path=None, **kwargs):
    global ALREADY_COPIED
    if ALREADY_COPIED: return
    global FILES_TO_COPY
    if file_Path is None: file_Path = Path(get_file_path_form_kwargs(**kwargs))
    dir_Path = file_Path.parent.absolute()
    user_folder_Path = get_User_folder_Path()
    D(f"user_folder_Path = {user_folder_Path}")
    for f2c_dict in FILES_TO_COPY:
        file_name_to_copy = f2c_dict['file_name_to_copy']
        D(f"file_name_to_copy = {file_name_to_copy}")
        new_name = f2c_dict['new_name']
        D(f"new_name = {new_name}")
        file_name_exception = f2c_dict['except_if_in_folder_there_is']
        D(f"file_name_exception = {file_name_exception}")
        D(f"{file_name_exception} in os.listdir(dir_Path) ? {file_name_exception in os.listdir(dir_Path)}")
        if file_name_exception in os.listdir(dir_Path): continue
        source_Path = user_folder_Path / file_name_to_copy
        destination_Path = dir_Path / new_name
        D(f"source_Path = {source_Path}")
        D(f"destination_Path = {destination_Path}")
        copy_folder_or_file(source_Path, destination_Path)
    ALREADY_COPIED = True



def can_a_venv_be_created_here(abs_Path):
    global VENV_NOT_ALLOWED_FILE_NAMES
    if not os.path.isdir(abs_Path): abs_Path = Path(abs_Path).parent
    D(f"can_a_venv_be_created_here?\n\tpath:'{abs_Path}")
    set_of_file_names = set(os.listdir(abs_Path))
    common_files = set_of_file_names.intersection(VENV_NOT_ALLOWED_FILE_NAMES)
    D(f"common_files:\n\t{common_files}")
    if common_files: 
        # global FILE2INTERPRETER_DICT
        # FILE2INTERPRETER_DICT = False
        D("\t-> NO")
        return False
    else: 
        D("\t-> YES")
        return True


def handle_pipenv_venv(**kwargs):
    file_path = get_file_path_form_kwargs(**kwargs)
    if not can_a_venv_be_created_here(file_path): return kwargs
    python_interpreter = find_or_create_python_interpreter(**kwargs)
    D(f"python_interpreter = {python_interpreter}")
    kwargs = change_kwargs_cmd_python_interpreter(python_interpreter, **kwargs)
    D(f"kwargs:\n\t{kwargs}")
    return kwargs


def change_kwargs_cmd_python_interpreter(python_interpreter, **kwargs):
    old_cmd = kwargs['cmd']
    new_cmd = [python_interpreter] + old_cmd[1:]
    kwargs['cmd'] = new_cmd
    # D(f"new_cmd = {new_cmd}")
    # kwargs['working_dir'] = ""
    # D(f"kwargs['working_dir'] = {kwargs['working_dir']}")
    return kwargs



def find_or_create_python_interpreter(file_Path=None, **kwargs):
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT is None: 
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    # D(f"FILE2INTERPRETER_DICT:\n\t{FILE2INTERPRETER_DICT}")
    if file_Path is None: file_Path = Path(get_file_path_form_kwargs(**kwargs))
    D(f"file_Path = {file_Path}")
    file_abs_path = str(Path(file_Path).absolute())
    D(f"file_abs_path = {file_abs_path}")
    if not does_file_exists(file_abs_path): 
        raise_file_path_does_not_exists(file_abs_path)
    pipenv_venv = get_pipenv_of_file(file_abs_path)
    D(f"pipenv_venv = {pipenv_venv}")
    # D(f"pipenv_venv == None ? {pipenv_venv == None}")
    # D(f"pipenv_venv is None ? {pipenv_venv is None}")
    if pipenv_venv is None:
        D(f"SINCE pipenv_venv == None")
        create_pipenv_venv(file_abs_path)
        pipenv_venv = subprocess_check_which_venv(file_abs_path)
        D(f"pipenv_venv = {pipenv_venv}")
    python_interpreter = pipenv_venv + "\\Scripts\\python.exe"
    # file_name = Path(__file__).stem
    # D(f"file_name = {file_name}")
    # D(f"kwargs = {kwargs}")
    return python_interpreter



def does_var_exist(variable_name: str) -> bool:
    if variable_name in locals(): return True
    if variable_name in globals(): return True



def one_time_operation(func): #UNUSED
    def wrap(*args, **kwargs):
        global_var_name = "was_function_" + func.__name__ + "_performed"
        if not does_var_exist(global_var_name): globals()[global_var_name] = False
        elif globals()[global_var_name] == True: return
        # D(f"{global_var_name} = {globals()[global_var_name]}")
        # D(func.__name__)
        result = func(*args, **kwargs)
        globals()[global_var_name] = True
        return result
    return wrap



def does_file_exists(file_abs_path): 
    return os.path.exists(file_abs_path)



def get_folder_of_file(abs_path):
    if os.path.isdir(abs_path): return abs_path
    folder = os.path.dirname(abs_path)
    return folder



def get_path_without_suffix(path):
    abs_path = Path(path).absolute()
    suffixes = abs_path.suffixes
    D(f"suffixes = {suffixes}")
    tot_len = 0
    for s in suffixes: tot_len += len(s)
    abs_path = str(abs_path)
    path_without_suffix = abs_path[:-tot_len]
    return path_without_suffix



def is_a_subfolder_of_b(a:str, b:str):
    if a == b[:len(a)]: return True
    else: return False



def get_abs_path_for_pickled_dict():
    # D(f"__file__ = {__file__}")
    path_without_suffix = get_path_without_suffix(__file__)
    # D(f"path_without_suffix = {path_without_suffix}")
    abs_path = path_without_suffix+'_file2interpreter_dict'+'.pkl'
    D(f"abs_path = {abs_path}")
    return abs_path

def save_file2interpreter_dictionary():
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT == False: return
    if FILE2INTERPRETER_DICT is None:
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    abs_path = get_abs_path_for_pickled_dict()
    with open(abs_path, 'wb') as f:
        pickle.dump(FILE2INTERPRETER_DICT, f)

def load_file2interpreter_dictionary():
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT == False: return
    abs_path = get_abs_path_for_pickled_dict()
    with open(abs_path, 'rb') as f:
        file2interpreter_dict = pickle.load(f)
    return file2interpreter_dict

def add_entry_to_file2interpreter_dictionary(file_path, pipenv_venv):
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT == False: return
    if FILE2INTERPRETER_DICT is None:
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    D(f"file_path = {file_path}")
    D(f"pipenv_venv = {pipenv_venv}")
    assert os.path.isfile(file_path)
    assert os.path.isfolder(pipenv_venv)
    assert os.path.exists(file_path)
    assert os.path.exists(pipenv_venv)
    FILE2INTERPRETER_DICT[file_path] = pipenv_venv
    save_file2interpreter_dictionary()


def subprocess_run_commands(iterable):
    if type(iterable) is str: 
        return subprocess_run_single_command(cmd=iterable)
    elif isinstance(iterable, Iterable):
        cmd = ' && '.join(iterable)
        D(f"cmd = {cmd}")
        return subprocess_run_single_command(cmd)

def subprocess_run_single_command(cmd):
    sub_output = subprocess.run(
        cmd, 
        capture_output=True, 
        universal_newlines=True, 
        text=True, 
        shell=True, 
        encoding = "utf-8" 
    )
    output = sub_output.stdout + sub_output.stderr
    # D(f"output.strip() = \n{output.strip()}")
    return output



def get_pipenv_of_file(file_path):
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT == False: return
    if FILE2INTERPRETER_DICT is None:
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    # D(f"FILE2INTERPRETER_DICT:\n\t{FILE2INTERPRETER_DICT}")
    for key_file_path, pipenv_venv in FILE2INTERPRETER_DICT.items():
        # D(f"key_file_path = {key_file_path}")
        # D(f"pipenv_venv = {pipenv_venv}")
        if is_a_subfolder_of_b(a=file_path, b=key_file_path):
            # D(f">>>\tfile_path:\n\t'{file_path}'\n\tis in key:\n\t'{key_file_path}'")
            if not os.path.exists(pipenv_venv): return None
            return pipenv_venv
    pipenv_venv = subprocess_check_which_venv(file_path)
    return pipenv_venv

def subprocess_check_which_venv(file_path):
    folder_path = get_folder_of_file(file_path)
    D(f"folder_path = {folder_path}")
    cmds = (f"cd {folder_path}", f"pipenv --venv")
    output = subprocess_run_commands(cmds).replace("\n", "")
    # D(f"output = {output}")
    initial_err_msg = "No virtualenv has been created for this project"
    final_err_msg = "yet!Aborted!"
    if (
        output[:len(initial_err_msg)] == initial_err_msg and 
        output[-len(final_err_msg):] == final_err_msg
    ):
        # D("ERRORS FOUND")
        # raise_file_path_does_not_have_a_pipenv_folder(file_path)
        return None
    else:
        # D("no error found")
        add_entry_to_file2interpreter_dictionary(
            file_path, 
            pipenv_venv:=output,
        )
    return pipenv_venv

def create_pipenv_venv(abs_Path):
    if not os.path.isdir(abs_Path): abs_Path = Path(abs_Path).parent
    cmds = (
        f"cd {abs_Path}",
        f"pipenv shell",
        f"pipenv sync", # Creates the venv and if the folder already
                        # has a pipfile.Lock it downloads all dependencies.
    )
    D(f"running cmd:\n\t{cmds}")
    output = subprocess_run_commands(cmds).replace("\n", "")
    cmds = (
        f"cd {abs_Path}",
        f"pipenv lock", #If there is not a .lock create one. DOES NOT WORK
    )
    D(f"running cmd:\n\t{cmds}")
    output = subprocess_run_commands(cmds).replace("\n", "")



def raise_file_path_does_not_have_a_pipenv_folder(file_path):
    err_msg =  f"File:\n'{file_path}'\nIS NOT INSIDE A 'pipenv folder'!\n"
    err_msg += f"   1. Please choose a folder that defines this project.\n"
    err_msg += f"   2. Using cmd promt 'cd' to said folder.\n"
    err_msg += f"   3. Then use the command 'pipenv shell' to create a 'pipenv folder'."
    sublime.message_dialog(err_msg)
    raise ValueError(err_msg)

def raise_file_path_does_not_exists(file_path):
    err_msg =  f"File:\n'{file_path}'\nDOES NOT EXIST!\n"
    sublime.message_dialog(err_msg)
    raise ValueError(err_msg)
```