# Things to note about \_\_import\_\_
- When calling "`import __init__`" only the first `__init__.py` file is called, it NEEDS to be in the folder.<br>I have automated the process when using the [[Sublime Text - Index|Sublime Text IDE]].
	- Here's the plugin: [[Sublime Text - Pluign for python 'good practices' • Code • myPython|'myPython' plugin]]
   *~Ex.:* Folder Structure like:
	```
	Package\
		+-- SubPackage\
		+-- __init__.py
		+-- sub_function.py
	+-- __init__.py
	+-- function.py
	```
   And in both `function.py` and  `sub_function.py` there is the following line of code:
	```python
		import __init__
	```
   Then, both the `Package\SubPackage\__init__.py` and `Package\__init__.py` will be executed.
----
###### Code:
```python
import sys
import os
import builtins
import importlib.util
import types
from pathlib import Path
import inspect
import re



ACCEPTED_SUFFIX_FOR_IMPORT = (
    ".py",
    ".pyx", # extensions of cython files
)

DECIDE_IF_FILE_IS_ALLOWED_FOR_IMPORT = (
	lambda abs_Path: abs_Path.suffix in ACCEPTED_SUFFIX_FOR_IMPORT,
	lambda abs_Path: abs_Path.name != "__init__.py",
	lambda abs_Path: are_all_chars_allowed(abs_Path),
)

DECIDE_IF_DIR_IS_ALLOWED_FOR_IMPORT = (
	lambda abs_Path: is_PyPackage(abs_Path) or does_folder_cotain_a_pyx_file(abs_Path),
	lambda abs_Path: abs_Path.name != "__pycache__",
	lambda abs_Path: are_all_chars_allowed(abs_Path),
)

def is_PyPackage(abs_Path):
	return "__init__.py" in os.listdir(abs_Path)

def does_folder_cotain_a_pyx_file(abs_Path):
	for item in os.listdir(abs_Path):
		extension = Path(item).suffix
		if extension == ".pyx": return True
	return False

def are_all_chars_allowed(abs_Path):
	remaning_str = abs_Path.with_suffix("").name
	remaning_str = re.sub(r'[A-Z]', '', remaning_str)
	remaning_str = re.sub(r'[a-z]', '', remaning_str)
	remaning_str = re.sub(r'[0-9]', '', remaning_str)
	remaning_str = re.sub('_', '', remaning_str)
	return remaning_str == ""



# -----------------------------------------------------------------



def is_allowed_for_import(abs_Path):
	if os.path.isfile(abs_Path):
		global DECIDE_IF_FILE_IS_ALLOWED_FOR_IMPORT
		for function in DECIDE_IF_FILE_IS_ALLOWED_FOR_IMPORT:
			if not function(abs_Path): return False
		return True
	if os.path.isdir(abs_Path):
		global DECIDE_IF_DIR_IS_ALLOWED_FOR_IMPORT
		for function in DECIDE_IF_DIR_IS_ALLOWED_FOR_IMPORT:
			if not function(abs_Path): return False
		return True
	return False



def listdir_full_Path(abs_Path):
	add_abs_Path = lambda x: abs_Path / x
	return tuple(map(add_abs_Path, os.listdir(abs_Path)))



def get_root_folder(file_abs_Path = Path(__file__)):
	father_Path = file_abs_Path.parent
	if not is_allowed_for_import(father_Path): return file_abs_Path
	else: return get_root_folder(father_Path)



ROOT_FOLDER = get_root_folder()
FATHER_DIR = ROOT_FOLDER.parent



def does_string_ends_with(str_, word): 
	return str_[-len(word):] == word



def fast_getattr(obj, attr):
	try: return obj.__dict__[attr]
	except KeyError:
		error = KeyError(attr)
		if sys.version_info >= (3, 11): # requires Python >= 3.11
			new_module_name = obj.__name__.replace(".__init__","")
			err_msg =  f"\t'{new_module_name}' has no attribute called '{attr}'\n"
			err_msg += f"\tIts attributes are:\n\t>>>\t{dir(obj)}"
			error.add_note(err_msg) 
		raise error

def load_module(Lazy_Module):
		if Lazy_Module.__is_loaded__: return
		Lazy_Module.__is_loaded__ = True
		name = Lazy_Module.__name__
		module = Lazy_Module.__module__
		loader = Lazy_Module.__loader__
		file = Lazy_Module.__file__
		if not file: return
		is_package = does_string_ends_with(file, "\\__init__.py")
		if is_package: return
		sys.modules[name] = module
		loader.exec_module(module)


class Lazy_Module(types.ModuleType):
	def __init__(self, module):
		super().__init__(module.__name__)
		self.__module__ = module
		self.__is_loaded__ = False
		self.__dict__.update(module.__dict__)

	def __call__(self, *args, **kwargs):
		load_module(self)
		if self.__name__ in self.__module__.__dict__:
			foo = fast_getattr(self.__module__, self.__name__)
			return foo(*args, **kwargs)
		else:
			err_msg  = f"Cannot find attribute '{self.__name__}' in Lazy_Module:\n\t"
			err_msg += f"{self}"
			raise NameError(err_msg)

	def __getattr__(self, name):
		load_module(self)
		try: return fast_getattr(self.__module__, name)
		except RuntimeError as e:
			err_msg = str(e)
			err_msg += "\n\t---------------------------------\n"
			err_msg += "\t>>> if thise error is about a CYTHON file:\n"
			err_msg += "\t>>> REMEMBER that for cython files:\n"
			err_msg += "\t>>> YOU CANNOT RELAOD THEM!\n"
			err_msg += "\t>>> so call them from only 1 function each time!\n\n"
			raise RuntimeError(err_msg)

	def __str__(self):
		if self.__is_loaded__:
			return f"<LOADED Lazy_Module '{self.__name__}' from: '{self.__file__}'>"
		else:
			return f"<UNLOADED Lazy_Module '{self.__name__}' from: '{self.__file__}'>"



def get_path_relative_to(father_Path, child_Path):
	father_path = str(father_Path)
	child_path = str(child_Path)
	if len(father_path) > len(child_path): return None
	father_path = father_path.replace("\\","/")
	child_path = child_path.replace("\\","/")
	splitted_father_path = father_path.split("/")
	splitted_child_path = child_path.split("/")
	count = 0
	for i in range(len(splitted_father_path)):
		if splitted_father_path[i] != splitted_child_path[i]: break
		count += 1
	if count != len(splitted_father_path): return None
	else: return "/".join(splitted_child_path[count:])



def lazy_import(abs_Path):
	old_sys_path = sys.path
	father_dir = str(abs_Path.parent)
	if father_dir not in sys.path: sys.path.append(father_dir)
	name = abs_Path.with_suffix("").name
	spec = importlib.util.find_spec(name)
	module = importlib.util.module_from_spec(spec)
	lazy_module = Lazy_Module(module)
	sys.path = old_sys_path
	return lazy_module



def get_sys_key_from_path(abs_Path):
	Path_without_extension = abs_Path.with_suffix("")
	relative_path = get_path_relative_to(FATHER_DIR, Path_without_extension)
	return relative_path.replace("/",".")



def add_all_absolute_imports_to_sys_modules(abs_Path = ROOT_FOLDER):
	def add_new_sys_key(abs_Path, output_list):
		if not is_allowed_for_import(abs_Path): return
		sys_key = get_sys_key_from_path(abs_Path)
		sys.modules[sys_key] = lazy_import(abs_Path)
		output_list.append(sys_key)

	def recursive_function(abs_Path, added_sys_keys):
		for item_Path in listdir_full_Path(abs_Path):
			add_new_sys_key(item_Path, added_sys_keys)
			if os.path.isdir(item_Path):
				recursive_function(item_Path, added_sys_keys)

	added_sys_keys = list()
	add_new_sys_key(abs_Path, added_sys_keys)
	recursive_function(abs_Path, added_sys_keys)
	return added_sys_keys



def bound_attributes_to_submodules(keys_to_bound):
	for sys_key in keys_to_bound:
		if "." not in sys_key: continue
		splitted_sys_key = sys_key.split(".")
		parent_module_key = ".".join(splitted_sys_key[:-1])
		attribute = splitted_sys_key[-1]
		if not parent_module_key in sys.modules.keys(): continue
		setattr(sys.modules[parent_module_key], attribute, sys.modules[sys_key])



def add_sys_key_shortcut_for_this_subfolder(keys_to_reference):
	this_file_Path = Path(__file__)
	folder_Path = this_file_Path.parent
	package_name = folder_Path.name
	sys_key = list(filter(
		lambda x: does_string_ends_with(x, package_name), 
		keys_to_reference
	))
	assert len(sys_key) == 1
	sys_key = sys_key[0]
	sys.modules[package_name] = sys.modules[sys_key]



def lazy_import_all_modules_and_submodules_in_this_package():
	added_sys_keys = add_all_absolute_imports_to_sys_modules()
	bound_attributes_to_submodules(keys_to_bound = added_sys_keys)
	# For niche corner cases:
	# In case there IS an __init__.py file, and you import the package:
	add_sys_key_shortcut_for_this_subfolder(
		keys_to_reference = added_sys_keys
	)



lazy_import_all_modules_and_submodules_in_this_package()
sys.modules["__init__"] = lambda: None



def is_file_in_this_package(file_Path): 
	relative_path =  get_path_relative_to(FATHER_DIR, file_Path)
	return relative_path != None



old_import_function = builtins.__import__

def new_import_function(*args, **kwargs):
	try: file_Path = Path(args[1]["__file__"])
	except (KeyError, IndexError): return old_import_function(*args, **kwargs)

	if not is_file_in_this_package(file_Path): return old_import_function(*args, **kwargs)

	old_module_name = args[1]["__name__"]
	sys_key = get_sys_key_from_path(file_Path)
	if does_string_ends_with(sys_key, ".__init__"):
		sys_key = sys_key[:-len(".__init__")]
	sys.modules[old_module_name] = sys.modules[sys_key]
	relative_path = get_path_relative_to(FATHER_DIR, file_Path)
	new_module_name = relative_path.replace("/", ".").replace(".py","")
	if does_string_ends_with(new_module_name, ".__init__"):
		new_module_name = new_module_name[:-9]
	old_package = args[1]["__package__"]
	splitted_new_package = new_module_name.split('.')[:-1]
	new_package = '.'.join(splitted_new_package)
	args[1]["__name__"] = new_module_name
	args[1]["__package__"] = new_package
	
	out =  old_import_function(*args, **kwargs)
	
	args[1]["__name__"] = old_module_name
	args[1]["__package__"] = old_package
	return out

builtins.__import__ = new_import_function

```