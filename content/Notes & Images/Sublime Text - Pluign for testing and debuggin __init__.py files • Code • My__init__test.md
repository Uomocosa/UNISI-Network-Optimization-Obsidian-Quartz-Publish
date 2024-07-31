###### How to make it work
1. Find your ***Sublime Text/User Folder***, it should be somenthing like:<br>`C:\Users\Uomocosa\AppData\Roaming\Sublime Text\Packages\User`.
2. Create two new files:
	- `My__init__test.sublime-build` 
	- `My__init__test.py` 
3. Create at least a folder called "*`test_1_`*" in the correct path, inside this folder you can create some simple python package strucutre, with blank "*`__init__.py`*" files.
4. Then create a new "`*__init__to_copy.py*`" file, this will be the file that will get copied to all instances of the other "*`__init__.py`*" files,  in onether new folder, taking "*`test_1_`*" as template.
5. In Sublime Text go to: `Tools >> Build System >> My__init__test`, and build it.<br>==***NOTE***: There is a section in the code of the `My__init__test.py`  file that need to be edited, specifically you need to define the corrects *paths* to the folders.==
---
###### My__init__test.sublime-build
```json
{
    "target": "my__init__test", 
    //Refering to: My__init__testCommand
    // "name": "build ALL executable files",
    "selector": "source.python",
    "cmd": ["py", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "env": {"PYTHONIOENCODING": "utf-8"},
    "encoding": "utf-8",

    "variants":
    [
        {
            "name": "build only the FIRST executable file",
            "variant_id": "001",
        },
    ]
}

```

---
###### My__init__test.py
```python
import sublime
import sublime_plugin
import subprocess
import os
import pathlib
import shutil
import time

DEBUG = True
def D(debug_message): 
    if DEBUG: print(">>> "+debug_message) 

# ---------------------- Changables -----------------------------
ALLOWED_FILE_NAMES = ["__init__to_be_copied", "__init__da_copiare"]

FOLDER_TO_SAVE_TEST_SUBFOLDERS = {
    'Simone-PC': "C:\\Users\\acer\\Desktop\\Samuele\\Syncthing\\LWF - LightWeigth Folder\\[P] Python\\Various Tests\\Test_Various_inits",
    'Uomocsa-PC': "D:\\Program Files (x86)\\Syncthing\\LWF - LightWeigth Folder\\[P] Python\\Various Tests\\Test_Various_inits",
}

TEMPLATE_TEST_FOLDERS = {
    'Simone-PC': "C:\\Users\\acer\\AppData\\Roaming\\Sublime Text\\Packages\\User\\my__init__test_folders",
    'Uomocsa-PC': "C:\\Users\\Uomocosa\\AppData\\Roaming\\Sublime Text\\Packages\\User\\my__init__test_folders",
}

EXECUTABLE_FILE_EXTENSIONS = [".py"]
EXCLUDE_THESE_EXECUTABLE_FILES = ["__init__.py"]

CURRENT_PC = None
# ---------------------- ---------- -----------------------------

list_of_PCs = list(FOLDER_TO_SAVE_TEST_SUBFOLDERS.keys())
# D(f"list_of_PCs = {list_of_PCs}")




class My__init__testCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        current_PC = get_current_pc()
        D(f"current_PC = {current_PC}")
        __init__file_path = kwargs['cmd'][2]
        assert_correct_file_name(__init__file_path)
        save_folder_path = FOLDER_TO_SAVE_TEST_SUBFOLDERS[current_PC]
        new_Test_folder_path = create_new_Test_folder()
        add_test = lambda test_folder_name : add_modified_subtest_folder_to_folder(
            destination_test_folder=new_Test_folder_path, 
            subtest_folder_name=test_folder_name,
            new__init__file_path=__init__file_path,
        )
        test_1_abs_path = add_test("test_1_")
        list_of_executable_files = get_executable_files_in_folder(test_1_abs_path)
        D(f"list_of_executable_files = {list_of_executable_files}")
        D(f"kwargs:\n\t{kwargs}")
        variant_id = get_variant_id(kwargs)
        D(f"kwargs:\n\t{kwargs}")
        if variant_id == 1 : # "build only the FIRST executable file"
            kwargs['cmd'][2] = list_of_executable_files[0]
            self.window.run_command("exec", kwargs)
        else: # default, execute ALL
            self.execute_each_file(list_of_executable_files, kwargs)
        # D("THIS IS AFTER EXEC COMMAND")
        # self.window.run_command("exec", kwargs)
        # add_test("test_2_")
        # add_test("test_3_")



    def execute_each_file(self, list_of_executable_files, kwargs):
        def async_recursive(i):
            if i >= len(list_of_executable_files): return
            # Execute file 'i'
            kwargs['cmd'][2] = list_of_executable_files[i]
            self.window.run_command("exec", kwargs)
            wait_time = (i+1)*1000
            D(f"wait_time = {wait_time}")
            # Schedule the next iteration
            sublime.set_timeout_async(lambda: async_recursive(i+1), wait_time)
        async_recursive(i=0)



def get_variant_id(kwargs):
    if 'variant_id' in kwargs.keys():
        variant_id = int(kwargs.get('variant_id'))
        del kwargs['variant_id']
    else: 
        variant_id = 0
    D(f"variant_id:\n\t{variant_id}")
    return variant_id



def get_current_pc():
    global CURRENT_PC
    if CURRENT_PC is not None: return CURRENT_PC
    else:
        global FOLDER_TO_SAVE_TEST_SUBFOLDERS
        global TEMPLATE_TEST_FOLDERS
        folder_to_save_was_found = False
        template_folder_was_found = False
        output_PC = None
        for PC, folder_to_save in FOLDER_TO_SAVE_TEST_SUBFOLDERS.items():
            D(f"PC = {PC} : folder_to_save = {folder_to_save}")
            if does_path_exists(folder_to_save):
                folder_to_save_was_found = True
                if PC in TEMPLATE_TEST_FOLDERS.keys():
                    template_folder = TEMPLATE_TEST_FOLDERS[PC]
                    if does_path_exists(template_folder): 
                        CURRENT_PC = PC
                        return CURRENT_PC
        for PC, template_folder in TEMPLATE_TEST_FOLDERS.items():
            D(f"PC = {PC} : template_folder = {template_folder}")
            if does_path_exists(folder_to_save): template_folder_was_found = True

        if folder_to_save_was_found==False and template_folder_was_found==False:
            err_msg =  f"NONE OF THESE FOLDERS WAS FOUND:\n"
            err_msg += f"TEMPLATE_TEST_FOLDERS:\n{TEMPLATE_TEST_FOLDERS}"
            err_msg += f"\n\nALSO, NONE OF THESE FOLDERS WAS FOUND:\n"
            err_msg += f"FOLDER_TO_SAVE_TEST_SUBFOLDERS:\n{FOLDER_TO_SAVE_TEST_SUBFOLDERS}"
        elif folder_to_save_was_found==True and template_folder_was_found==False:
            err_msg =  f"NONE OF THESE FOLDERS WAS FOUND:\n{TEMPLATE_TEST_FOLDERS}"
        elif folder_to_save_was_found==False and template_folder_was_found==True:
            err_msg =  f"NONE OF THESE FOLDERS WAS FOUND:\n{FOLDER_TO_SAVE_TEST_SUBFOLDERS}"
        elif folder_to_save_was_found==True and template_folder_was_found==True:
            err_msg =  f"I think there is an error on the following definitions:"
            err_msg += f"\n\nTEMPLATE_TEST_FOLDERS:\n{TEMPLATE_TEST_FOLDERS}"
            err_msg += f"\n\nFOLDER_TO_SAVE_TEST_SUBFOLDERS:\n{FOLDER_TO_SAVE_TEST_SUBFOLDERS}"
        err_msg += f">>> Please add/correct it by changing this file:\n{__file__}"
        sublime.message_dialog(err_msg)
        raise ValueError(err_msg)
        


def assert_correct_file_name(file_abs_path):
    global ALLOWED_FILE_NAMES
    # D(f"file_abs_path = {file_abs_path}")
    # D(f"get_file_name_without_suffix(file_abs_path) = {get_file_name_without_suffix(file_abs_path)}")
    if get_file_name_without_suffix(file_abs_path) not in ALLOWED_FILE_NAMES:
        raise_not_correct_file(ALLOWED_FILE_NAMES[0])



def create_new_Test_folder():
    D(f"Entering: create_new_Test_folder")
    global FOLDER_TO_SAVE_TEST_SUBFOLDERS
    current_PC = get_current_pc()
    destination_path = FOLDER_TO_SAVE_TEST_SUBFOLDERS[current_PC]
    all_save_folders = os.listdir(destination_path)
    last_saved_folder_number = 0
    for folder_name in all_save_folders:
        if does_string_starts_with(folder_name, "Test_"):
            test_number = int(get_numeric_chars(folder_name))
            # D(f"test_number = {test_number}")
            if test_number > last_saved_folder_number: 
                last_saved_folder_number = test_number
    new_folder_name = "Test_" + str(last_saved_folder_number + 1)
    D(f"new_folder_name = {new_folder_name}")
    new_Test_folder_abs_path = destination_path+"\\"+new_folder_name
    D(f"new_Test_folder_abs_path = {new_Test_folder_abs_path}")
    assert not does_path_exists(abs_path)
    # if not DEBUG: 
    os.mkdir(new_Test_folder_abs_path)
    return new_Test_folder_abs_path



def is_executable_file(file_name):
    global EXECUTABLE_FILE_EXTENSIONS
    global EXCLUDE_THESE_EXECUTABLE_FILES
    file_Path = pathlib.Path(file_name)
    # D(f"file_Path = {file_Path}")
    D(f"file_Path.name = {file_Path.name}")
    # D(f"file_Path.suffix = {file_Path.suffix}")
    if file_Path.name in EXCLUDE_THESE_EXECUTABLE_FILES: return False
    for extension in EXECUTABLE_FILE_EXTENSIONS:
        if file_Path.suffix == extension: return True
    return False

def get_executable_files_in_folder(abs_folder_path):
    items = get_list_of_all_files_in_folder_and_subfolders(abs_folder_path)
    # D(f"items = {items}")
    files = filter(lambda x: os.path.isfile(x), items)
    # D(f"files = {files}")
    executable_files = filter(lambda x: is_executable_file(x), files)
    # D(f"executable_files = {executable_files}")
    return list(executable_files)



def does_string_starts_with(str_, word):
    if str_[:len(word)] == word: return True
    else: return False

def does_string_ends_with(str_, word):
    if str_[-len(word):] == word: return True
    else: return False



def get_numeric_chars(input_str):
    return ''.join([char for char in input_str if char.isdigit()])



def add_modified_subtest_folder_to_folder(
    destination_test_folder, subtest_folder_name, new__init__file_path
):
    global FOLDER_TO_SAVE_TEST_SUBFOLDERS
    global TEMPLATE_TEST_FOLDERS
    current_PC = get_current_pc()
    list_template_folders = list(os.listdir(TEMPLATE_TEST_FOLDERS[current_PC]))
    if not subtest_folder_name in list_template_folders:
        raise_A_not_found_in_list(A=subtest_folder_name, list_=list_template_folders)
    source_path = TEMPLATE_TEST_FOLDERS[current_PC]+"\\"+subtest_folder_name
    destination_path = destination_test_folder+"\\"+subtest_folder_name
    # if not DEBUG: 
    copy_folder_or_file(source_path, destination_path)
    replace_all__init__files_in_folder_with_the_current_one(destination_path, new__init__file_path)
    return destination_path



def replace_all__init__files_in_folder_with_the_current_one(folder, new__init__file_path):
    all_sub_paths = get_list_of_all_files_in_folder_and_subfolders(folder)
    D(f"all_sub_paths:\n\t{all_sub_paths}")
    old__init__paths = filter(
        lambda str_: does_string_ends_with(str_, "__init__.py"), 
        all_sub_paths
    )
    for old__init__file_path in old__init__paths:
        D(f"old__init__file = {old__init__file_path}")
        os.remove(old__init__file_path)
        copy_folder_or_file(source_path=new__init__file_path, destination_path=old__init__file_path)



def get_list_of_all_files_in_folder_and_subfolders(starting_path):
    def recursive_function(starting_path, list_=list()):
        list_.append(starting_path)
        if os.path.isdir(starting_path):
            for item in os.listdir(starting_path):
                abs_path = starting_path+"\\"+item
                recursive_function(abs_path, list_)
    output_list = list()
    recursive_function(starting_path, output_list)
    return output_list



def copy_folder_or_file(source_path, destination_path):
    if os.path.isdir(source_path):
        shutil.copytree(source_path, destination_path)
    if os.path.isfile(source_path):
        shutil.copyfile(source_path, destination_path)



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
    if not does_path_exists(file_abs_path): raise_file_path_does_not_exists(file_abs_path)
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



def does_path_exists(abs_path): 
    return os.path.exists(abs_path)



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



def get_file_name_without_suffix(path):
    return pathlib.Path(path).stem



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
    assert os.path.isdir(pipenv_venv)
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
    err_msg =  f"\nFile:\n'{file_path}'\nIS NOT INSIDE A 'pipenv folder'!\n"
    err_msg += f"   1. Please choose a folder that defines this project.\n"
    err_msg += f"   2. Using cmd promt 'cd' to said folder.\n"
    err_msg += f"   3. Then use the command 'pipenv shell' to create a 'pipenv folder'."
    sublime.message_dialog(err_msg)
    raise ValueError(err_msg)

def raise_file_path_does_not_exists(file_path):
    err_msg =  f"File:\n'{file_path}'\nDOES NOT EXIST!\n"
    sublime.message_dialog(err_msg)
    raise ValueError(err_msg)

def raise_not_correct_file(file_name):
    err_msg =  f"File name should be:\n'{file_name}'\n"
    err_msg += f"PLEASE CHANGE BUILD, OR GO TO THE CORRECT FILE\n"
    sublime.message_dialog(err_msg)
    raise ValueError(err_msg)

def raise_A_not_found_in_list(A, list_):
    err_msg =  f"ELEMENT {A} SHOULD HAVE BEEN FOUND IN LIST:'\n"
    err_msg += f"{list_}\n"
    sublime.message_dialog(err_msg)
    raise ValueError(err_msg)
```