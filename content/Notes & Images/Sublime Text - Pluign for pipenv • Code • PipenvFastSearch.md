###### How to make it work
1. Find your ***Sublime Text/User Folder***, it should be somenthing like:<br>`C:\Users\Uomocosa\AppData\Roaming\Sublime Text\Packages\User`.
2. Create two new files:
	- `PipenvFastSearch.sublime-build` 
	- `PipenvFastSearch.py` 
3. In any another folder in your pc, [[Python - pipenv • (pipenv) README.txt • Python Virtual Environment • Create a New pipenv venv|create a pipenv venv]], and create your project.
4. In Sublime Text go to: `Tools >> Build System >> PipenvFastSearch`, and build it.<br>The build system, will find the associeted python interpreter and will use that to build your code.<br>==***NOTE***: The first time you build a new file, it will be slower.==
---
###### PipenvFastSearch.sublime-build
```json
{
    "target": "pipenv_fast_search", //Refering to: PipenvFastSearchCommand
    "selector": "source.python",
    "cmd": ["py", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "env": {"PYTHONIOENCODING": "utf-8"},
    "encoding": "utf-8"
}
```

---
###### PipenvFastSearch.py
```python
import sublime
import sublime_plugin
import subprocess
import os
import pathlib
import pickle 

FILE2INTERPRETER_DICT = None
DEBUG = True

# POSSIBLE PROBLEMS and or future upgrades:
#   >>> The file related to FILE2INTERPRETER_DICT, may become too big,
#       so loading and saving may become a problem, to solve this a method
#       to reduce its size, may be deleting old entries, or creating a smarter
#       function, like one that finds the '.pipfile' and saves only that folder as key,
#       all other subfolder, are not saved.

class PipenvFastSearchCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        if DEBUG: print("PipenvFastSearchCommand")
        python_interpreter = find_python_interpreter(**kwargs)
        if DEBUG: print(f">>> python_interpreter = {python_interpreter}")
        kwargs = change_kwargs_cmd_python_interpreter(python_interpreter, **kwargs)
        if DEBUG: print(f">>> kwargs:\n\t{kwargs}")
        self.window.run_command("exec", kwargs)
        # save_file2interpreter_dictionary(FILE2INTERPRETER_DICT)



def change_kwargs_cmd_python_interpreter(python_interpreter, **kwargs):
    old_cmd = kwargs['cmd']
    new_cmd = [python_interpreter] + old_cmd[1:]
    kwargs['cmd'] = new_cmd
    # if DEBUG: print(f">>> new_cmd = {new_cmd}")
    # kwargs['working_dir'] = ""
    # if DEBUG: print(f">>> kwargs['working_dir'] = {kwargs['working_dir']}")
    return kwargs



def find_python_interpreter(**kwargs):
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT is None: 
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    # if DEBUG: print(f">>> FILE2INTERPRETER_DICT:\n\t{FILE2INTERPRETER_DICT}")
    file_abs_path = kwargs['cmd'][2]
    # if DEBUG: print(f">>> file_abs_path = {file_abs_path}")
    if not does_file_exists(file_abs_path): raise_file_path_does_not_exists(file_abs_path)
    pipenv_venv = get_pipenv_of_file(file_abs_path)
    # if DEBUG: print(f">>> pipenv_venv = {pipenv_venv}")
    python_interpreter = pipenv_venv + "\\Scripts\\python.exe"
    # file_name = pathlib.Path(__file__).stem
    # if DEBUG: print(f">>> file_name = {file_name}")
    # if DEBUG: print(f">>> kwargs = {kwargs}")
    return python_interpreter



def does_var_exist(variable_name: str) -> bool:
    if variable_name in locals(): return True
    if variable_name in globals(): return True



def one_time_operation(func): #UNUSED
    def wrap(*args, **kwargs):
        global_var_name = "was_function_" + func.__name__ + "_performed"
        if not does_var_exist(global_var_name): globals()[global_var_name] = False
        elif globals()[global_var_name] == True: return
        # if DEBUG: print(f"{global_var_name} = {globals()[global_var_name]}")
        # if DEBUG: print(func.__name__)
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
    abs_path = pathlib.PurePosixPath(path)
    suffixes = abs_path.suffixes
    if DEBUG: print(f">>> suffixes = {suffixes}")
    tot_len = 0
    for s in suffixes: tot_len += len(s)
    abs_path = str(abs_path)
    path_without_suffix = abs_path[:-tot_len]
    return path_without_suffix



def is_a_subfolder_of_b(a:str, b:str):
    if a == b[:len(a)]: return True
    else: return False



def get_abs_path_for_pickled_dict():
    # if DEBUG: print(f"__file__ = {__file__}")
    path_without_suffix = get_path_without_suffix(__file__)
    # if DEBUG: print(f"path_without_suffix = {path_without_suffix}")
    abs_path = path_without_suffix+'_file2interpreter_dict'+'.pkl'
    if DEBUG: print(f">>> abs_path = {abs_path}")
    return abs_path

def save_file2interpreter_dictionary():
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT is None:
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    abs_path = get_abs_path_for_pickled_dict()
    with open(abs_path, 'wb') as f:
        pickle.dump(FILE2INTERPRETER_DICT, f)

def load_file2interpreter_dictionary():
    abs_path = get_abs_path_for_pickled_dict()
    with open(abs_path, 'rb') as f:
        file2interpreter_dict = pickle.load(f)
    return file2interpreter_dict

def add_entry_to_file2interpreter_dictionary(file_path, pipenv_venv):
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT is None:
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    if DEBUG: print(f"file_path = {file_path}")
    if DEBUG: print(f"pipenv_venv = {pipenv_venv}")
    assert os.path.isfile(file_path)
    assert os.path.isfolder(pipenv_venv)
    assert os.path.exists(file_path)
    assert os.path.exists(pipenv_venv)
    FILE2INTERPRETER_DICT[file_path] = pipenv_venv
    save_file2interpreter_dictionary()




def subprocess_run_command(cmd):
    sub_output = subprocess.run(
        cmd, 
        capture_output=True, 
        universal_newlines=True, 
        text=True, 
        shell=True, 
        encoding = "utf-8" 
    )
    output = sub_output.stdout + sub_output.stderr
    # if DEBUG: print(f"output.strip() = \n{output.strip()}")
    return output



def get_pipenv_of_file(file_path):
    global FILE2INTERPRETER_DICT
    if FILE2INTERPRETER_DICT is None:
        FILE2INTERPRETER_DICT = load_file2interpreter_dictionary()
    # if DEBUG: (f">>> FILE2INTERPRETER_DICT:\n\t{FILE2INTERPRETER_DICT}")
    for key_file_path, pipenv_venv in FILE2INTERPRETER_DICT.items():
        # if DEBUG: print(f">>> key_file_path = {key_file_path}")
        # if DEBUG: print(f">>> pipenv_venv = {pipenv_venv}")
        if is_a_subfolder_of_b(a=file_path, b=key_file_path):
            # if DEBUG: print(f">>>\tfile_path:\n\t'{file_path}'\n\tis in key:\n\t'{key_file_path}'")
            return pipenv_venv
    pipenv_venv = subprocess_check_which_venv(file_path)
    return pipenv_venv

def subprocess_check_which_venv(file_path):
    folder_path = get_folder_of_file(file_path)
    if DEBUG: print(f"folder_path = {folder_path}")
    cmd_1 = f"cd {folder_path}"
    cmd_2 = f"pipenv --venv"
    output = subprocess_run_command(cmd_1+" && "+cmd_2).replace("\n", "")
    # if DEBUG: print(f"output = {output}")
    initial_err_msg = "No virtualenv has been created for this project"
    final_err_msg = "yet!Aborted!"
    if output[:len(initial_err_msg)] == initial_err_msg and output[-len(final_err_msg):] == final_err_msg:
        # if DEBUG: print("ERRORS FOUND")
        raise_file_path_does_not_have_a_pipenv_folder(file_path)
        return None
    else:
        # if DEBUG: print("no error found")
        add_entry_to_file2interpreter_dictionary(file_path, pipenv_venv:=output)
    return pipenv_venv



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