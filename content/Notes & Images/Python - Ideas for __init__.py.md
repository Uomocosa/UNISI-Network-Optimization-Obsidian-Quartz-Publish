Important read: [The Cost of Small Modules](https://nolanlawson.com/2016/08/15/the-cost-of-small-modules/)

- The `import __init__` statement should only be inside the `ifmain` - `Test()` part of the code

- Once imported the `__init__` file should work for all folders, that is, it should set up rules for the import system to follow in the more general way possible, like:
	- All files and folders in from the root folder down should be loaded in the `sys.modules` as *Lazy_pyFolder*(the folders) and *Lazy_pyFile*
	- The `builtins.__import__` function has to be re-written to allow smart relative imports.

Have to decide if a *Lazy_pyFile* once called changes type to a function or not

- Also have to decide if i want the *Lazy_pyFile* class or prefer to modify again how the `builtins.__import__` works to allow the automatic switch once the module it's imported

##### This one looks good
modify the `builtins.__import__` such that if the module to be imported is a *Lazy_pyFile* import it as a function or a module
- Function if it has a callable with the same name
- Module if it does not

---
# Solution
![[__init__.py code (2022 - 12 - 16)]]