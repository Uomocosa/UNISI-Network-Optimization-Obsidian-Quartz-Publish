# Things to note about \_\_import\_\_
- Also look at: [[Python - Understanding builtins.__import__.canvas|Understanding builtins.__import__]]
- When calling "`import __init__`" each `__init__.py` file is called, when found in the folder, i thought that when 1 was succeffully called python would stop calling the others.
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
- **Customize the PathEntryFinder**:
	- Source: [Online Video](https://2021.pycon.org.au/program/T7Z9VE/)
	- ***Problems with MetaPathFinders and PathEntryFinders***:
		They do not work with relative import (`from . import function`), the process is alted when python calls `builtins.__import__()`.
	- *Boiler-plate code*:
	```python
	class MyCustomPathEntryFinder:
		def __init__(self, path_entry):
			self.path_entry = path_entry

		def find_spec(self, path):
			module_spec = search_module(
				path_entry = self.path_entry,
				path = path
			)
			return module_spec
	
	sys.path_hooks.insert(0, MyCustomPathEntryFinder)
	```
	- *Actual Customization*:
	```python
	def search_module(self, path):
		# code for finding the module ...
		return module_spec
	```
-
- *~Ex.:* `args[0]`, what i called `module_name_from_ads_import`
- If I call `SubP11.subfun111`
