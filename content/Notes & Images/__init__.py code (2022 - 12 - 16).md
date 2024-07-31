##### Future Versions:
- Need to implement usage for [[Python - Cython|cython files]] (ending in `.pyx`).
- Add global variables to `dir(module)`
- Speed up execution.

---
##### All things to NOTE:
> **NOTE**:
> All internal files to the package **must** have an `import __init__`

> **NOTE**:
> In all folders there is a `__init__.py` file (they are python packages)

##### Folder Structure
> **NOTE**:
> In all folders there is a `__init__.py` file (they are python packages)
```
Package\
	+-- P1\
		+-- SubP11\
			+-- __init__.py
			+-- subfun111.py
		+-- __init__.py
		+-- fun11.py
		+-- fun12.py
	+-- P2\
		+-- __init__.py
		+-- fun21.py
	+-- __init__.py
	+-- main.py
test_from_outside.py
```

##### \_\_init\_\_.py
All `__init__.py` must have this content
```python


import sys
import os
import builtins
import importlib.util
import types


FILES_NAMES_TO_EXCLUDE_FROM_IMPORT = (
	"__init__.py"
)


def is_pyFolder(folder_path):
	try: return "__init__.py" in os.listdir(folder_path)
	except NotADirectoryError: return False



def is_pyFile(file_path):
	try:
		file_path = str(file_path).replace("\\","/")
		file_name = file_path.split("/")[-1]
		return file_name not in FILES_NAMES_TO_EXCLUDE_FROM_IMPORT and file_name[-3:] == ".py"
	except IndexError:
		return False



def listdir_full_path(abs_path):
	add_abs_path = lambda x: abs_path + "/" + x
	return tuple(map(add_abs_path, os.listdir(abs_path)))



def get_father_dir(abs_path = __file__):
	return "/".join(abs_path.replace("\\","/").split("/")[:-1])



def get_root_folder(file_abs_path = __file__):
	father_path = get_father_dir(file_abs_path)
	if not is_pyFolder(father_path): return file_abs_path
	else: return get_root_folder(father_path)



ROOT_FOLDER = get_root_folder()
FATHER_DIR = get_father_dir(ROOT_FOLDER)


def load_module(Lazy_Module):
	#print(f"TRYING TO LOAD MODULE: {Lazy_Module.__name__}")
	Lazy_Module.__loader__.exec_module(Lazy_Module.__module__)
	Lazy_Module.__is_loaded__ = True


def fast_getattr(obj, attr):
	return obj.__dict__[attr]

class Lazy_Module(types.ModuleType):
	def __init__(self, module):
		#types.ModuleType.__init__(self, __name__) #for Python 2
		super().__init__(module.__name__) #for Python 3
		self.__module__ = module
		self.__is_loaded__ = False
		self.__dict__.update(module.__dict__)
	
	def __call__(self, *args, **kwargs):
		if not self.__is_loaded__: load_module(self)
		#module = load_module(self)
		foo = fast_getattr(self.__module__, self.__name__)
		return foo(*args, **kwargs)

	def __getattr__(self, name):
		if not self.__is_loaded__: load_module(self)
		return fast_getattr(self.__module__, name)





def subctract_path(father_path, child_path):
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





def lazy_import(abs_path):
	old_sys_path = sys.path
	sys.path.append(get_father_dir(abs_path))
	file_name = abs_path.split("/")[-1].replace(".py","")
	if is_pyFolder(abs_path):
		spec = importlib.util.find_spec(file_name)
	elif is_pyFile(abs_path):
		spec = importlib.util.spec_from_file_location(file_name, abs_path)
	else:
		raise FileNotFoundError(f"file '{file_name}' is neither a pyFile or pyFolder")
	loader = importlib.util.LazyLoader(spec.loader)
	spec.loader = loader
	module = importlib.util.module_from_spec(spec)
	#loader.exec_module(module)
	lazy_module = Lazy_Module(module)
	sys.path = old_sys_path
	return lazy_module






def get_sys_key_from_path(abs_path):
	relative_path = subctract_path(FATHER_DIR, abs_path)
	return relative_path.replace("/",".")





def add_all_absolute_imports_to_sys_modules(abs_path = ROOT_FOLDER):
	for pyFile in list(filter(is_pyFile, listdir_full_path(abs_path))):
		sys_key = get_sys_key_from_path(pyFile.replace(".py",""))
		sys.modules[sys_key] = lazy_import(pyFile)
	for pyModule in list(filter(is_pyFolder, listdir_full_path(abs_path))):
		sys_key = get_sys_key_from_path(pyModule)
		sys.modules[sys_key] = lazy_import(pyModule)
		add_all_absolute_imports_to_sys_modules(abs_path = pyModule)





def bound_sys_module_to_sub_modules(sys_key):
	if "." not in sys_key: return
	splitted_sys_key = sys_key.split(".")
	temp = ""
	for i in range(len(splitted_sys_key) - 1):
		temp += "." + splitted_sys_key[i]
		a = temp[1:]
		b = temp[1:] + "." + splitted_sys_key[i+1]
		#print(f"setattr(sys.modules[{a}], {splitted_sys_key[i+1]}, sys.modules[{b}])")
		setattr(sys.modules[a], splitted_sys_key[i+1], sys.modules[b])






def bound_sys_modules_to_each_other(abs_path = ROOT_FOLDER):
	for pyFile in list(filter(is_pyFile, listdir_full_path(abs_path))):
		sys_key = get_sys_key_from_path(pyFile.replace(".py",""))
		bound_sys_module_to_sub_modules(sys_key)
	for pyModule in list(filter(is_pyFolder, listdir_full_path(abs_path))):
		sys_key = get_sys_key_from_path(pyModule)
		sys.modules[sys_key] = lazy_import(pyModule)
		bound_sys_module_to_sub_modules(sys_key)
		bound_sys_modules_to_each_other(abs_path = pyModule)




root_folder_name = ROOT_FOLDER.split("/")[-1]
#print(f"root_folder_name = {root_folder_name}")
sys.modules[root_folder_name] = lazy_import(ROOT_FOLDER)
add_all_absolute_imports_to_sys_modules()
bound_sys_modules_to_each_other()





def is_file_in_this_package(path): 
	relative_path =  subctract_path(ROOT_FOLDER, path)
	#print(f"relative_path = {relative_path}")
	return relative_path != None





old_import_function = builtins.__import__


def new_import_function(*args, **kwargs):
	try: file_path = args[1]["__file__"].replace("\\","/")
	except (KeyError, IndexError): return old_import_function(*args, **kwargs)

	if not is_file_in_this_package(file_path): return old_import_function(*args, **kwargs)

	old_file_name = args[1]["__name__"]
	modules_to_import = args[3]
	steps_of_relative_import = args[4]
	relative_path = subctract_path(get_father_dir(ROOT_FOLDER), file_path).replace(".py","")
	new_file_name = relative_path.replace(".py","").replace("/",".")
	old_package = args[1]["__package__"]
	splitted_new_package = new_file_name.split('.')[:-1]
	new_package = '.'.join(splitted_new_package)
	args[1]["__name__"] = new_file_name
	args[1]["__package__"] = new_package
	
	out =  old_import_function(*args, **kwargs)
	
	if old_file_name == "__main__": args[1]["__name__"] = "__main__"
	args[1]["__package__"] = old_package
	return out


builtins.__import__ = new_import_function


```

##### test_from_outside.py
```python
import Package
print(dir(Test_27))
print(dir(Test_27.P1.fun11))
Test_27.P1.fun11()
```

##### main.py
> **NOTE**:
> All internal files to the package **must** have an `import __init__`
```python
import __init__
from . import P1

def main(*args):
	print(f"CALLED with args = {args}")
	P1.SubP11.subfun111()

if __name__ == '__main__':
	main()
```

##### fun11.py
```python
import __init__
import sys
#print("SYS.PATH")
#print(sys.path)
from .. import main
from . import fun12
from . import fun11

print("fun11.py")


def fun11():
	print("CALLED fun11")
	main()
	fun12()

if __name__ == '__main__':
	fun11()
```

