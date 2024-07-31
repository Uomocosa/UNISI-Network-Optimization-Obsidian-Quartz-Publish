# Index
In this file, are reported all tests I did on python imports, tring to understand how to use the "\__init\__.py" files, and to get to a point that i like and is easy to scale up.
All these examples should work:

# Possible Errors to look out for:
- \__init\__ does not disting between ".py" files and other files
<br>
- [[#Basic Import]]
- [[#Using __init __ py]]
- [[#Upgrade of __init __ py]]
- [[#Changing __init __ py for Sublime Text 4 Plugins]]

My Objective is to get to a point where i can call the function in another file like:

###### Home Folder/main.py
```python
from myPackage.Debug import D
```

###### Home Folder/myPackage/Debug/D.py
```python
def D(message):
	if DEBUG is True:
		print(message)
```

---
### Basic Import
Somenthing that works, easiest implementation, but a pain in the ass to import:

<br>

###### Directory View
```
Home_Folder/
+-- main.py
+-- src/
	+-- function1.py
```
<br>

###### Home Folder/src/function1.py
```python
def function1():
	print("DIOCANE")
```
<br>

###### Home Folder/main.py
```python
from .src.function1 import function1

function1()
```
---
<br>

### Using \__init\__.py
This implementation was somewhat better, still a HUGE pain to import, as it has **TOO MUCH** boilerplate code:
<br>

###### Directory View
```
Home_Folder/
+-- main.py
+-- function2
+-- src/
	+-- __init__.py
	+-- function1.py
```
<br>

###### Home Folder/src/function1.py
```python
def function1():
	print("DIOCANE")
```
<br>

###### Home Folder/src/function1.py
```python
def function2():
	print("PORCAMADONNA")
```
<br>

###### Home Folder/main.py
```python
import sys
import os
old_path = sys.path
#---
from pathlib import Path
def un_passo_indietro_bailando(child_path):
    return Path(child_path).resolve().parent
#---
father_dir = un_passo_indietro_bailando(__file__)
while "__init__.py" in os.listdir(father_dir):
    #print("found an __init__.py")
    father_dir = un_passo_indietro_bailando(father_dir)

#print(f"package_dir = {father_dir}")
sys.path.append(str(father_dir))


abs_path = str(__file__).replace("/","\\")
vector_of_abs_path = abs_path.split("\\")

myPackage_index = vector_of_abs_path.index("myPackage")

vector_of_relative_path_from_myPackage_dir = [
    vector_of_abs_path[myPackage_index],
    vector_of_abs_path[myPackage_index + 1]
]

relative_path_from_myPackage_dir = ".".join(
    vector_of_relative_path_from_myPackage_dir
)

import_from_major_folder = __import__(
    relative_path_from_myPackage_dir,
    globals(), locals(),
    [''],
    0
)

#sys.path.append(str(father_dir))

#--- ALL ABSOLUTE IMPORTs FROM 'myPackage'
from src import function2


# IMPORT FROM MAJOR FOLDER: 
# Decide the name of relative import
# name_of_import_chose = import_from_major_folder
thisFolder = import_from_major_folder
#Def[Major Folder]: A direct subfolder of "myPackage" folder
from thisFolder import function1
#---

sys.path.append(old_path)

#----------------------------------------------------------

function1()
function2()
```
<br>

###### Home Folder/src/\__init\__.py
```python
import os
import importlib
import importlib.util

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

def assert_not_a_prohibited_file_name(file_name:str) -> None:
    prohibited_file_names = (
        'globals.py',
        '__gloabls__.py',
        'gloabl.py',
        '__gloabl__.py',
    )
    if file_name in prohibited_file_names:
        err_msg = "\n\n >>> In python folder there cannot be a file named: "
        err_msg += f"'{file_name}'\n"
        raise NameError(err_msg)

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

def add_function_file_to_global_scope_from_file_absolute_path(file_absolute_path):
            file_name = file_absolute_path.split("\\")[-1]
            #print(f"file_name = {file_name}")
            spec = importlib.util.spec_from_file_location(file_name, file_absolute_path)
            #print(f"spec = {spec}")
            foo = importlib.util.module_from_spec(spec)
            #print(f"foo = {foo}")
            spec.loader.exec_module(foo) 
            file_name = file_name.replace(".py","")
            if file_name in dir(foo):
                #print(f"file_name is define as a function or class is in the file: {file_name}")
                #print(f"file_name = {file_name}")
                function = getattr(foo, file_name)
                #print(f"function = {function}")
                globals()[file_name] = function
                #print(f"file_name = {file_name}")

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

#Get directory containing this file
dir_absolute_path = __file__.replace("\\__init__.py","")


#Get list of all files and folders
file_list = os.listdir(dir_absolute_path)


#Add folders to path
for folder_name in file_list:
    path = dir_absolute_path + "\\" + folder_name
    if os.path.isdir(path) and folder_name != "__pycache__":
        #print(f"folder_name = {folder_name}")
        if __name__ != "__main__":
            #print(f"__name__ = {__name__}")
            module = importlib.import_module(f"{__name__}.{folder_name}")


#Add files.py to path
#print(f"file_list = {file_list}")
for file_name in file_list:
    #print()
    #print(f"file_name = {file_name}")
    if file_name[-3:] == ".py" and file_name != "__init__.py":
        assert_not_a_prohibited_file_name(file_name)
        file_absolute_path = dir_absolute_path + "\\" + file_name
        add_function_file_to_global_scope_from_file_absolute_path(file_absolute_path)
```

<br>

---

<br>

### Upgrade of \__init\__.py
This time the implementation is really small, just **1 line of code**, tho there is a little problem, at the time unsolvable, is that if I call `import Package1.SubPackage1.SubSubPackage1 as ssp` **it loads all of Package1 and its subpackages**, i would like it to load just  Package1.SubPackage1.SubSubPackage1, and leave the rest unloaded
<br>

###### Directory View
```
Home_Folder/
+-- main.py
+-- __init__.py
+-- src/
	+-- __init__.py
	+-- function1.py
	+-- function2.py
```
<br>

###### Home Folder/src/function1.py
```python
import __init__.py #Necessay only for TESTING this file alone

def function1():
	print("DIOCANE")
```
<br>

###### Home Folder/src/function2.py
```python
import __init__.py #Necessay only for TESTING this file alone

def function2():
	print("PORCAMADONNA")
```
<br>

###### Home Folder/main.py
```python
import src
src.function1()
src.function2()
```

###### Home Folder/\__init\__.py
```python
# you can leave this file empty
```

###### Home Folder/src/\__init\__.py
```python
import sys
import importlib
import inspect
import pathlib
import os
import copy

# PURE function
def convert_to_tuple(argument):
	return tuple(argument)

# PURE function
def get_abs_path_to_this_directory() -> str:
	abs_path_to_file = str(inspect.getfile(inspect.currentframe()))
	vec = abs_path_to_file.replace("\\","/").split("/")
	vec = vec[:-1]
	return "/".join(vec)

# PURE function
def get_list_of_entries_in(directory_abs_path) -> tuple:
	list_of_entries = os.listdir(directory_abs_path)
	return convert_to_tuple(list_of_entries)

# PURE function
def get_father_dir(directory_abs_path) -> str:
	dir_path = copy.copy(directory_abs_path)
	dir_path = dir_path.replace("\\","/")
	dir_path_vector = dir_path.split("/")
	dir_path_vector = dir_path_vector[:-1]
	dir_path = "/".join(dir_path_vector)
	return dir_path

# PURE function
def get_root_folder() -> str:
	this_directory = get_abs_path_to_this_directory()
	def recursive_function(current_dir, previous_dir = None):
		files_and_folders_in_this_dir = get_list_of_entries_in(current_dir)
		if '__init__.py' in files_and_folders_in_this_dir:
			father_dir = get_father_dir(current_dir)
			return recursive_function(father_dir, current_dir)
		else: return previous_dir
	root_folder = recursive_function(this_directory)
	return root_folder.replace("\\","/")

ROOT_FOLDER = get_root_folder()
sys.path.insert(1,ROOT_FOLDER)



if __name__ != "__init__" and __name__ != "__main__":

	# PURE function
	def remove_this_or_that_from_str(original_str, this, that):
		str1 = original_str.replace(this, "")
		str2 = original_str.replace(that, "")
		if len(str1) <= len(str2): return str1
		else: return str2
	
	# PURE function
	def remove_doubles(original_list: tuple) -> tuple:
		output_list = list()
		already_encountred = list()
		for item in original_list:
			if item not in already_encountred:
				already_encountred.append(item)
				output_list.append(item)
		return convert_to_tuple(output_list)
	
	# PURE function
	def remove_all(original_list: tuple, item_to_remove) -> tuple:
		output_list = list()
		for item in original_list:
			if item != item_to_remove:
				output_list.append(item)
		return convert_to_tuple(output_list)

	# PURE function
	def get_abs_path_to_this_file() -> str:
		return str(inspect.getfile(inspect.currentframe()))

	# PURE function
	def is_folder(absolute_path):
		return os.path.isdir(absolute_path)

	# PURE function
	def is_file(absolute_path):
		return os.path.isfile(absolute_path)

	# PURE function
	def get_all_sub_paths_from_folder(
		absolute_path, 	output = list()):
		if is_file(absolute_path):
			return (absolute_path,)
		entries_in_folder = get_list_of_entries_in(absolute_path)
		for entry in entries_in_folder:
			entry_abs_path = absolute_path + "/" + entry
			if is_folder(entry_abs_path):
				output.append(entry_abs_path)
				get_all_sub_paths_from_folder(entry_abs_path, output)
			else: output.append(entry_abs_path)
		return convert_to_tuple(output)

	# PURE function
	def path_first_step(absolute_path):
		copied_path = copy.copy(absolute_path)
		copied_path = copied_path.replace("\\","/")
		return copied_path.split("/")[0]

	# PURE function
	def path_last_step(absolute_path):
		copied_path = copy.copy(absolute_path)
		copied_path = copied_path.replace("\\","/")
		return copied_path.split("/")[-1]

	# PURE function
	def exclude_pycache_folders(special_list):
		otuput_list = list()
		PYCHACHE = "__pycache__"
		for abs_path in special_list:
			abs_path = abs_path.replace("\\", "/")
			#print(f"abs_path = {abs_path}")
			is_pycache_at_the_start = path_first_step(abs_path) == PYCHACHE
			is_pycache_in_the_middle = ('/'+PYCHACHE+'/') in abs_path
			is_pycache_at_the_end = path_last_step(abs_path) == PYCHACHE
			if not (
				is_pycache_at_the_start or 
				is_pycache_in_the_middle or 
				is_pycache_at_the_end
			): otuput_list.append(abs_path)
		return convert_to_tuple(otuput_list)
	
	# PURE function
	def exclude_init_files(abs_file_paths):
		otuput_list = list()
		INIT = "__init__.py"
		for abs_path in abs_file_paths:
			abs_path = abs_path.replace("\\", "/")
			#print(f"abs_path = {abs_path}")
			is_pycache_at_the_end = path_last_step(abs_path) == INIT
			if not (is_pycache_at_the_end): otuput_list.append(abs_path)
		return convert_to_tuple(otuput_list)

	# PURE function
	def divide_into_relative_folders_and_abs_file_paths(special_list):
		list_of_relative_folders = list()
		list_of_abs_file_paths = list()

		relative_path_from_ROOT_FOLDER = lambda absolute_path: absolute_path.replace(ROOT_FOLDER + "/","")

		for abs_path in special_list:
		#print(relative_path(abs_path))
			if is_file(abs_path):
				vector = abs_path.split("/")
				relative_path = relative_path_from_ROOT_FOLDER(abs_path)
				file_name = abs_path.split("/")[-1]
				#print(f"folder_path = {folder_path}")
				#print(f"relative_path(abs_path) = {relative_path(abs_path)}")
				relative_folder = remove_this_or_that_from_str(
					relative_path, file_name, "/"+file_name)
				list_of_relative_folders.append(relative_folder)
				list_of_abs_file_paths.append(abs_path)
				#print(f">>> relative_folder = {relative_folder},  file_name = {file_name}")
		return(
			convert_to_tuple(list_of_relative_folders), 
			convert_to_tuple(list_of_abs_file_paths))
	
	# IMPURE function
	def import_modules(modules_to_import: tuple) -> None:
		for module in modules_to_import:
			module = module.replace("/",".")
			importlib.import_module(module)
	
	# IMPURE function
	def import_method_functions_from_abs_file_paths(abs_file_paths: tuple) -> None:
		for abs_path in abs_file_paths:
			file_name = abs_path.split("/")[-1]
			#print(f"file_name = {file_name}")
			spec = importlib.util.spec_from_file_location(file_name, abs_path)
			foo = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(foo)
			file_name = file_name.replace(".py","")
			globals()[file_name] = getattr(foo, file_name)

	OUTPUT = get_all_sub_paths_from_folder(get_abs_path_to_this_directory())
	OUTPUT = exclude_pycache_folders(OUTPUT)

	relative_folders, abs_file_paths = divide_into_relative_folders_and_abs_file_paths(OUTPUT)
	abs_file_paths = exclude_init_files(abs_file_paths)

	modules_to_import = remove_doubles(relative_folders)
	modules_to_import = remove_all(modules_to_import, "")

	del divide_into_relative_folders_and_abs_file_paths
	del exclude_init_files
	del exclude_pycache_folders
	del get_abs_path_to_this_file
	del get_all_sub_paths_from_folder
	del is_file
	del is_folder
	del path_first_step
	del path_last_step
	del relative_folders
	del remove_all
	del remove_doubles
	del remove_this_or_that_from_str
	del OUTPUT

	import_modules(modules_to_import)
	import_method_functions_from_abs_file_paths(abs_file_paths)
	
	del modules_to_import
	del import_modules
	del import_method_functions_from_abs_file_paths
	del abs_file_paths

del ROOT_FOLDER
del sys
del importlib
del inspect
del pathlib
del os
del copy

del convert_to_tuple
del get_abs_path_to_this_directory
del get_list_of_entries_in
del get_father_dir
del get_root_folder
```

<br>

---

<br>

### Changing \_\_init\_\_.py for Sublime Text 4 Plugins
As it stands the sublime plugin are loading with an internal version of python, older than what i usally use, so the \__init\__.py is a litte different, also we have to change the folder using the sys path, especially in the main.py file, it also suffers from the same problem as the \__init\__ used in the normal python.


###### Directory View
```
Home_Folder/
+-- main.py
+-- __init__.py
+-- src/
	+-- __init__.py
	+-- function1.py
	+-- function2.py
```
<br>

###### Home Folder/src/function1.py
```python

def function1():
	print("DIOCANE")
```
<br>

###### Home Folder/src/function2.py
```python

def function2():
	print("PORCAMADONNA")
```
<br>

###### Home Folder/main.py
```python
# THIS CODE WILL ALWAYS BE HERE
import inspect
import sys
abs_path_to_file = str(inspect.getfile(inspect.currentframe()))
vec = abs_path_to_file.replace("\\","/").split("/")
PATH_TO_THIS_FOLDER = "/".join(vec[:-1])
if PATH_TO_THIS_FOLDER not in sys.path: sys.path.insert(1, PATH_TO_THIS_FOLDER)

# ACTUAL MAIN.PY CODE
import src
src.function1()
src.function2()
```
<br>

###### Home Folder/\__init\__.py
```python
#can be leaved empty
```

###### Home Folder/\__init\__.py
```python
FILES_NAMES_TO_EXCLUDE_FROM_IMPORT = [
    "__init__",
    "__config__",
    "__global__",
    "__globals__"
]

# OBJECTIVES:
#
# submodules_to_import = ("P1/SubP11/SubSubP111")
#   SHOULD BE ALL PACKAGES FROM PARENT FOLDER AND THIS FOLDER
#
# functions_to_import = ("P1/SubP11/subfun111")
#   SHOULD BE ALL FUNCTIONS IN THIS FOLDER


import functools
import importlib
import imp
import inspect
import os
import sys

def T(argument: any) -> tuple:
    if type(argument) is str: return tuple((argument,))
    else: return tuple(argument)

def S(argument: any) -> str:
    if type(argument) is tuple: return "".join(argument)
    else: return str(argument)

# PURE function
def get_abs_path_to_this_directory() -> str:
    abs_path_to_file = S(inspect.getfile(inspect.currentframe()))
    vec = abs_path_to_file.replace("\\","/").split("/")
    vec = vec[:-1]
    return "/".join(vec)

# PURE function
def get_list_of_entries_in(directory_abs_path) -> tuple:
    if not os.path.isdir(directory_abs_path): return None
    list_of_entries = os.listdir(directory_abs_path)
    return T(list_of_entries)

# PURE function
def get_father_dir(directory_abs_path) -> str:
    directory_abs_path = directory_abs_path.replace("\\","/")
    dir_path_vector = directory_abs_path.split("/")
    dir_path_vector = dir_path_vector[:-1]
    dir_path = "/".join(dir_path_vector)
    return dir_path

# PURE function
def get_root_folder() -> str:
    this_directory = get_abs_path_to_this_directory()
    def recursive_function(current_dir, previous_dir = None):
        files_and_folders_in_this_dir = get_list_of_entries_in(current_dir)
        if '__init__.py' in files_and_folders_in_this_dir:
            father_dir = get_father_dir(current_dir)
            return recursive_function(father_dir, current_dir)
        else: return previous_dir
    root_folder = recursive_function(this_directory)
    return root_folder.replace("\\","/")

def get_this_folder_path() -> str:
    abs_path_to_file = str(inspect.getfile(inspect.currentframe()))
    vec = abs_path_to_file.replace("\\","/").split("/")
    return "/".join(vec[:-1])


def get_all_entries_names_in(path):
    return T(filter(lambda x: x != None, get_list_of_entries_in(path)))

def get_all_subpaths_in(path):
    return T(map(lambda x: path + "/" + x, get_all_entries_names_in(path)))

def get_all_folders_paths_in(path):
    return T(filter(lambda x: os.path.isdir(x), get_all_subpaths_in(path)))

def get_all_files_paths_in(path):
    return T(filter(lambda x: os.path.isfile(x), get_all_subpaths_in(path)))

def is_python_package(path):
    if not os.path.isdir(path): return False
    else: return '__init__.py' in get_all_entries_names_in(path)

def ends_with(string, ending):
    return string[-len(ending):] == ending

def get_last_step_of_path(path):
    return path.split("/")[-1]

def is_python_file(path):
    if not os.path.isfile(path): return False
    else: return ends_with(get_last_step_of_path(path), ".py")

def get_all_python_submodules_in(path):
    if not is_python_package(path): return None
    else: return T(filter(is_python_package, get_all_subpaths_in(path)))

def get_all_python_files_in(path):
    return T(filter(is_python_file, get_all_subpaths_in(path)))

def remove_extension_from_file_path(path: str) -> str:
    if "." not in path: return path
    return ".".join(path.split(".")[:-1])

def delete_one_instance_from_tuple(input_tuple, instance_to_remove) -> tuple:
    return T(filter(lambda x: x != instance_to_remove, input_tuple))

def delete_all_instances_from_tuple(input_tuple, instances_to_remove) -> tuple:
    for inst in instances_to_remove: 
        input_tuple = delete_one_instance_from_tuple(input_tuple, inst)
    return input_tuple

ROOT_FOLDER = get_root_folder()
if __name__ == "__init__": sys.path.insert(1, ROOT_FOLDER)

THIS_FOLDER = get_this_folder_path()
assert is_python_package(ROOT_FOLDER)
submodules_abs_paths = get_all_python_submodules_in(THIS_FOLDER)
functions_abs_paths = get_all_python_files_in(THIS_FOLDER)
functions_names_abs_paths = T(map(remove_extension_from_file_path, functions_abs_paths))

get_relative_path = lambda s: s.replace(ROOT_FOLDER+"/", "")
submodules_rel_paths = T(map(get_relative_path, submodules_abs_paths))
functions_names_rel_paths = T(map(get_relative_path, functions_names_abs_paths))

FILES_NAMES_TO_EXCLUDE_FROM_IMPORT = T(map(
    remove_extension_from_file_path, FILES_NAMES_TO_EXCLUDE_FROM_IMPORT))
has_to_exclude_file = (
    lambda s: get_last_step_of_path(s) not in FILES_NAMES_TO_EXCLUDE_FROM_IMPORT)
functions_names_rel_paths = T(filter(has_to_exclude_file, functions_names_rel_paths))

submodules_rel_paths = T(map(lambda s: s.replace("/","."), submodules_rel_paths))

# -------------------------------------------------------------
# ------------------------- IMPURE FUNCTIONS ------------------
# -------------------------------------------------------------

def import_my_function_from_relative_path(relative_path: str) -> None:
    fun_name = S(relative_path.split("/")[-1])
    method_path_to_fun = relative_path.replace("/",".")
    globals()[fun_name] = importlib.import_module(method_path_to_fun)
    imp.reload(globals()[fun_name])
    globals()[fun_name] = getattr(globals()[fun_name], fun_name)

#importlib.import_module("P1.SubP11")
T(map(import_my_function_from_relative_path, functions_names_rel_paths))
T(map(importlib.import_module, submodules_rel_paths))

del FILES_NAMES_TO_EXCLUDE_FROM_IMPORT
del ROOT_FOLDER
del THIS_FOLDER
del S
del T
del delete_all_instances_from_tuple
del delete_one_instance_from_tuple
del ends_with
del functions_abs_paths
del functions_names_abs_paths
del functions_names_rel_paths
del functools
del get_abs_path_to_this_directory
del get_all_entries_names_in
del get_all_files_paths_in
del get_all_folders_paths_in
del get_all_python_files_in
del get_all_python_submodules_in
del get_all_subpaths_in
del get_father_dir
del get_last_step_of_path
del get_list_of_entries_in
del get_relative_path
del get_root_folder
del get_this_folder_path
del has_to_exclude_file
del imp
del import_my_function_from_relative_path
del importlib
del inspect
del is_python_file
del is_python_package
del os
del remove_extension_from_file_path
del submodules_abs_paths
del submodules_rel_paths
del sys
```

