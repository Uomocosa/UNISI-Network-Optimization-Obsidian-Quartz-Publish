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
import sys, os, types, re
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



def get_dict_keys(mod):
	return mod.__module__.__dict__.keys()

def get_attr(mod, attr):
	return mod.__module__.__dict__[attr]

def getattr_from_Lazy_Module(Lazy_Module, attr):
	if attr in get_dict_keys(Lazy_Module): 
		return get_attr(Lazy_Module, attr)

	original_file_Path = Path(Lazy_Module.__file__)
	add_submodules_dynamically(original_file_Path)
	file_Path = Path(Lazy_Module.__file__)
	abs_sys_key = get_abs_sys_key_from_Path(file_Path)
	searched_key = abs_sys_key + "." + attr
	if searched_key in sys.modules.keys():
		return sys.modules[searched_key]

	load_module(Lazy_Module)
	if attr in get_dict_keys(Lazy_Module): 
		return get_attr(Lazy_Module, attr)

	error = KeyError(attr)
	if sys.version_info >= (3, 11): # requires Python >= 3.11
		new_module_name = Lazy_Module.__name__.replace(".__init__","")
		err_msg =  f"\t'{new_module_name}' has no attribute called '{attr}'\n"
		err_msg += f"\tIts attributes are:\n\t>>>\t{get_dict_keys(Lazy_Module)}"
		error.add_note(err_msg) 
	raise error

def load_module(Lazy_Module):
		if Lazy_Module.__is_loaded__: return
		Lazy_Module.__is_loaded__ = True
		# name = Lazy_Module.__name__
		module = Lazy_Module.__module__
		loader = Lazy_Module.__loader__
		file_Path = Path(Lazy_Module.__file__)
		if file_Path.name == "__init__.py": return
		abs_sys_key = get_abs_sys_key_from_Path(file_Path)
		sys.modules[abs_sys_key] = module
		loader.exec_module(module)
		return module


class Lazy_Module(types.ModuleType):
	def __init__(self, module, abs_Path):
		# print(f">>> Lazy_Module, module.__name__ = {module.__name__}")
		super().__init__(module.__name__)
		self.__module__ = module
		self.__is_loaded__ = False
		self.__dict__.update(module.__dict__)
		self.__file__ = abs_Path

	def __call__(self, *args, **kwargs):
		# print(f"__call__, self.__name__ = {self.__name__}")
		load_module(self)
		if self.__name__ in self.__module__.__dict__:
			foo = getattr_from_Lazy_Module(self, self.__name__)
			return foo(*args, **kwargs)
		else:
			err_msg  = f"Cannot find attribute '{self.__name__}' in Lazy_Module:\n\t"
			err_msg += f"{self}"
			raise NameError(err_msg)

	def __getattr__(self, name):
		try: return getattr_from_Lazy_Module(self, name)
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



def get_root_folder(file_abs_Path = Path(__file__)):
	father_Path = file_abs_Path.parent
	if not is_allowed_for_import(father_Path): return file_abs_Path
	else: return get_root_folder(father_Path)



def lazy_import(abs_Path, rel_sys_key):
	old_sys_path = sys.path
	father_dir = str(abs_Path.parent)
	if father_dir not in sys.path: sys.path.append(father_dir)
	name = abs_Path.with_suffix("").name
	spec = importlib.util.find_spec(name)
	module = importlib.util.module_from_spec(spec)
	abs_sys_key = get_abs_sys_key_from_Path(abs_Path)
	sys.modules[abs_sys_key] = Lazy_Module(module, abs_Path)
	if rel_sys_key != abs_sys_key: 
		sys.modules[rel_sys_key] = sys.modules[abs_sys_key]
		# print(f"sys.modules[{rel_sys_key}] = sys.modules[{abs_sys_key}]")
	sys.path = old_sys_path



def get_or_create_active_sys_key_of(abs_Path):
	if abs_Path.name == "__init__.py": abs_Path = abs_Path.parent
	submodule_name = abs_Path.name

	last_submodule = lambda module_road: module_road.split(".")[-1]
	for sys_key in sys.modules:
		if "." not in sys_key: continue
		if last_submodule(sys_key) == submodule_name:
			# print(f">>> found already-created sys_key: '{sys_key}'")
			return sys_key

	lazy_import(abs_Path, submodule_name)
	return submodule_name



def add_submodules_dynamically(abs_Path):
	sys_key = get_or_create_active_sys_key_of(abs_Path)

	if not os.path.isdir(abs_Path): abs_Path = abs_Path.parent
	for item_Path in listdir_full_Path(abs_Path):
		if is_allowed_for_import(item_Path):
			attr = item_Path.with_suffix("").name
			new_sys_key = sys_key + "." + attr
			lazy_import(item_Path, new_sys_key)
			abs_sys_key = get_abs_sys_key_from_Path(item_Path.parent)
			new_sys_key = abs_sys_key + "." + attr
			# print(f">>> setattr({abs_sys_key}, {attr}, {new_sys_key})")
			setattr(sys.modules[abs_sys_key], attr, sys.modules[new_sys_key])


def Start():
	lazy_import(ROOT_FOLDER, ROOT_FOLDER.name)
	THIS_DIR = Path(__file__).parent
	add_submodules_dynamically(THIS_DIR)


ROOT_FOLDER = get_root_folder()
FATHER_DIR = ROOT_FOLDER.parent
Start()


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

	old_module_name = args[1]["__name__"]
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