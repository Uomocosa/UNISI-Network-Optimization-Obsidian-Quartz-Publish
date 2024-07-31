# Things to note about \_\_import\_\_
- When calling "`import __init__`" only the first `__init__.py` file is called, it NEEDS to be in the folder.<br>I have automated the process when using the [[Sublime Text - Index|Sublime Text IDE]].
	- Here's the plugin: [[Sublime Text - Pluign for python 'good practices' • Code • myPython|'myPython' plugin]]<br>*~Ex.:* Folder Structure like:
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
import sys, os, re
import types, inspect
import importlib.util
import builtins
from pathlib import Path

# print(f">I> __init__.py\n\tLOCATED at:\n\t\t{__file__}")

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



def does_string_ends_with(str_, word): 
	return str_[-len(word):] == word



def get_abs_sys_key_from_Path(abs_Path):
	if abs_Path.name == "__init__.py": abs_Path = abs_Path.parent
	Path_without_extension = abs_Path.with_suffix("").absolute()
	relative_path = get_path_relative_to(FATHER_DIR, Path_without_extension)
	return relative_path.replace("/",".")



class Lazy_Module(types.ModuleType):
	def __init__(self, module, abs_Path):
		super().__init__(module.__name__)
		self.__module_from_spec__ = module
		self.__is_loaded__ = False
		self.__dict__.update(module.__dict__)
		self.__file__ = abs_Path

	def __call__(self, *args, **kwargs):
		return call_Lazy_Module(self, *args, **kwargs)

	def __getattr__(self, attr):
		return get_attr_Lazy_Module(self, attr)

	def __str__(self):
		return f"<Lazy_Module '{self.__name__}' from: '{self.__file__}'>"

	def __dir__(self):
		return get_dir_Lazy_Module(self)



def get_root_folder(file_abs_Path = Path(__file__)):
	father_Path = file_abs_Path.parent
	if not is_allowed_for_import(father_Path): return file_abs_Path
	else: return get_root_folder(father_Path)



def get_rel_sys_key_from_Path(abs_Path):
	if abs_Path.name == "__init__.py": abs_Path = abs_Path.parent
	Path_without_extension = abs_Path.with_suffix("").absolute()
	relative_path = get_path_relative_to(RELATIVE_FOLDER.parent, Path_without_extension)
	if relative_path is None: return None
	return relative_path.replace("/",".")

def lazy_import(abs_Path):
	if abs_Path.name == "__init__.py": abs_Path = abs_Path.parent
	if not is_allowed_for_import(abs_Path): return
	old_sys_path = sys.path
	father_dir = str(abs_Path.parent)
	if father_dir not in sys.path: sys.path.append(father_dir)
	name = abs_Path.with_suffix("").name
	spec = importlib.util.find_spec(name, abs_Path)
	module = importlib.util.module_from_spec(spec)
	abs_sys_key = get_abs_sys_key_from_Path(abs_Path)
	rel_sys_key = get_rel_sys_key_from_Path(abs_Path)
	# print(f"\t>> abs_sys_key = {abs_sys_key} | rel_sys_key = {rel_sys_key}")
	sys.modules[abs_sys_key] = Lazy_Module(module, abs_Path)
	# print(f"\t>> sys.modules[{abs_sys_key}] = Lazy_Module(module, abs_Path)")
	if rel_sys_key and rel_sys_key != abs_sys_key:
		sys.modules[rel_sys_key] = sys.modules[abs_sys_key]
		# print(f"\t\t> sys.modules[{rel_sys_key}] = sys.modules[{abs_sys_key}]")
	sys.path = old_sys_path



def load_submodules(abs_Path):
	if not os.path.isdir(abs_Path): return
	allowed_Paths = filter(is_allowed_for_import, listdir_full_Path(abs_Path))
	get_sys_key_end = lambda module_road: module_road.split(".")[-1]
	get_father_sys_key = lambda module_road: ".".join(module_road.split(".")[:-1])
	# print(f">>> sys.modules.keys() = {sys.modules.keys()}")
	for item_Path in allowed_Paths:
		abs_sys_key = get_abs_sys_key_from_Path(item_Path)
		lazy_import(item_Path)
		attr = get_sys_key_end(abs_sys_key)
		father_sys_key = get_father_sys_key(abs_sys_key)
		# Lazy_Module.__dict__[attr] = sys.modules[abs_sys_key]
		# print(f">>> setattr({father_sys_key}, {attr}, {abs_sys_key})")
		setattr(sys.modules[father_sys_key], attr, sys.modules[abs_sys_key])



def unite_Lazy_Module_and_module_dicts(Lazy_Module, module):
	is_attr_module = lambda attr: inspect.ismodule(attr)
	dict_to_save = dict()
	for key, attr in module.__dict__.items():
		if is_attr_module(attr): continue
		if key in Lazy_Module.__dict__: continue
		dict_to_save[key] = attr
	# print(f">>> dict_to_save = {dict_to_save}")
	Lazy_Module.__dict__.update(dict_to_save)
	# print(Lazy_Module.__file__)

def load_last_submodule(Lazy_Module):
	# print(f">F> 'load_last_submodule' for: {Lazy_Module.__name__}")
	# print(f"LOADING: {Lazy_Module.__name__}")
	abs_Path = Lazy_Module.__file__
	if os.path.isdir(abs_Path): return
	name = Lazy_Module.__name__
	module = Lazy_Module.__module_from_spec__
	loader = Lazy_Module.__loader__
	loader.exec_module(module)
	unite_Lazy_Module_and_module_dicts(Lazy_Module, module)



def load_module(Lazy_Module):
	# print(f">F> Is LOADED?: {Lazy_Module.__is_loaded__}")
	if Lazy_Module.__is_loaded__: return
	Lazy_Module.__is_loaded__ = True
	abs_Path = Lazy_Module.__file__
	load_submodules(abs_Path)
	load_last_submodule(Lazy_Module)



def get_attr_Lazy_Module(Lazy_Module, attr):
	# print(f">F> 'get_attr_Lazy_Module' for: {Lazy_Module.__name__}")
	load_module(Lazy_Module)
	if attr in Lazy_Module.__dict__.keys():
		return Lazy_Module.__dict__[attr]
	# else:
		# err_msg = "TODO err_msg"
		# raise err_msg



def call_Lazy_Module(Lazy_Module, *args, **kwargs):
	# print(f">F> 'call_Lazy_Module' for: {Lazy_Module.__name__}")
	load_module(Lazy_Module)
	if Lazy_Module.__name__ in Lazy_Module.__module_from_spec__.__dict__.keys():
		foo = Lazy_Module.__module_from_spec__.__dict__[Lazy_Module.__name__]
		return foo(*args, **kwargs)



def get_dir_Lazy_Module(Lazy_Module):
	# print(f">F> 'get_dir_Lazy_Module' for: {Lazy_Module.__name__}")
	load_module(Lazy_Module)
	return Lazy_Module.__dict__



def import_up_to_relative():
	lazy_import(ROOT_FOLDER) #start absolute imports
	if RELATIVE_FOLDER == ROOT_FOLDER: return
	def recursive_function(abs_Path):
		if abs_Path == ROOT_FOLDER: return
		lazy_import(abs_Path)
		recursive_function(abs_Path.parent)
	recursive_function(RELATIVE_FOLDER)

def Setup():
	# print(f">>> ROOT_FOLDER = {ROOT_FOLDER}")
	lazy_import(ROOT_FOLDER) #start absolute imports
	import_up_to_relative()
	# for k in sys.modules: print(f">>> k = {k} : {isinstance(sys.modules[k], Lazy_Module)}")
	sys.modules["__init__"] = lambda: None


ROOT_FOLDER = get_root_folder()
FATHER_DIR = ROOT_FOLDER.parent
RELATIVE_FOLDER = Path(__file__).parent
Setup()





def from_relative_import_do_absolute_imports(*args):
	# form the python docs on __import__:
	name = args[0]
	globals_ = args[1]
	locals_ = args[2]
	fromlist = args[3]
	level = args[4]
	# print(f">>> globals_ = {globals_}")
	# print(f">>> locals_ = {locals_}")
	caller_file = globals_['__file__']
	# searched_module = globals_['__name__']
	# package = globals_['__package__']
	# print(f">>> name = {name}")
	# print(f">>> caller_file = {caller_file}")
	# print(f">>> package = {package}")
	# print(f">>> searched_module = {searched_module}")
	# print(f">>> fromlist = {fromlist}")
	if level == 0: level = 1

	if name in sys.modules: 
		mod = sys.modules[name]
		if isinstance(mod, Lazy_Module):
			load_module(mod)
			# print(mod)
			# print(f">>> returning EARLY mod: '{name}'")
			new_args = (name, globals_, locals_, fromlist, 0)
			# return mod
			return old_import_function(*new_args)
		# print(f">>> FOUND '{name}' in sys.modules, but it's not a Lazy_Module")
		return old_import_function(*args)
	abs_Path = Path(caller_file)
	if abs_Path.name == "__init__.py": abs_Path = abs_Path.parent
	# print(f">>> abs_Path = {abs_Path}")
	for _ in range(level): abs_Path = abs_Path.parent
	# print(f">>> abs_Path = {abs_Path}")
	abs_sys_key = get_abs_sys_key_from_Path(abs_Path)
	if name and abs_sys_key: abs_sys_key = abs_sys_key + "." + name
	if name and not abs_sys_key: abs_sys_key = name
	# print(f">>> abs_sys_key = {abs_sys_key}")
	module_key_road = abs_sys_key.split(".")
	sys_key = module_key_road[0]
	if sys_key not in sys.modules:
		return old_import_function(*args)
	for sub_key in module_key_road[1:]:
		if sub_key in dir(sys.modules[sys_key]):
			sys_key = sys_key + "." + sub_key
		else:
			# print(f">>> did NOT found {sub_key} in {sys_key}")
			return old_import_function(*args)
	mod = sys.modules[sys_key]
	if isinstance(mod, Lazy_Module):
		load_module(mod)
		# print(f">>> returning mod: '{sys_key}'")
		return mod
	# print(f">>> final sys_key = {sys_key}")
	new_args = (sys_key, globals_, locals_, fromlist, 0)
	return old_import_function(*new_args)



def is_file_in_this_package(file_Path): 
	relative_path =  get_path_relative_to(FATHER_DIR, file_Path)
	return relative_path != None



old_import_function = builtins.__import__

def new_import_function(*args, **kwargs):
	try: 
		file_Path = Path(args[1]["__file__"])
	except (KeyError, IndexError): 
		return old_import_function(*args, **kwargs)
	
	if not is_file_in_this_package(file_Path):
		return old_import_function(*args, **kwargs)

	out =  from_relative_import_do_absolute_imports(*args)
	# print(f">>> out = {out}")
	return out

builtins.__import__ = new_import_function
```