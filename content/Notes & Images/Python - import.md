- ***Sources***:
	-  [[Python - The Import System]] **REALLY REALLY GOOD & INDEPT TALK**
		- [Youtube - David Beazley (PyCon2015)](https://www.youtube.com/watch?v=MCs5OvhV9S4)
	- [Handful Guide](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#:~:text=root%20test%2F%20folder.-,What%20is%20an%20import%20%3F,made%20available%20to%20the%20importer.)
	- [[Python - __import__(...)]]
		- [Official Documentation](https://docs.python.org/3/library/functions.html#:~:text=Note%20This%20is%20an%20advanced%20function%20that%20is%20not%20needed%20in%20everyday%20Python%20programming%2C%20unlike)
	- [[Python - Importers]]
		- [Youtube from 'Sreekanth'](https://www.youtube.com/watch?v=QCSz0j8tGmI): **REALLY** good youtube video, explains the sequence for importing a module, looking also at the memory location, and where the module is saved.
		- [Youtube from 'SF Python'](https://www.youtube.com/watch?v=NRynSD6MCLE): it explains the concepts, and show some code behind [importlib.machinery](https://docs.python.org/3/library/importlib.html#:~:text=importlib/machinery.py-,This%20module%20contains%20the%20various%20objects%20that%20help,-import%20find%20and), to create your own **Finders** and **Loaders**, (together they form an **IMPORTER**)
	- [[Python - Absolutes and Relative Imports]]
	- [[Python - Understanding builtins.__import__.canvas|Python - Understanding builtins.__import__]]
	- [[Python - HOW I IMPORT - My __init__.py Files]]

---
## Summary / Key Points

-   `import` statements search through the list of paths in `sys.path`
-   `sys.path` always includes the path of the script invoked on the command line and is agnostic to the working directory on the command line.
-   importing a package is conceptually the same as importing that package’s `__init__.py` file
---
## Basic Definitions

-   **module**: any `*.py` file. Its name is the file name.
-   **built-in module**: a “module” (written in C) that is compiled into the Python interpreter, and therefore does not have a `*.py` file.
-   **package**: any folder containing a file named `__init__.py` in it. Its name is the name of the folder.
    -   in Python 3.3 and above, any folder (even without a `__init__.py` file) is considered a package
-   **object**: in Python, almost everything is an object - functions, classes, variables, etc.
----
## Example Directory Structure

```
test/                      # root folder
	packA/                 # package packA
		subA/              # subpackage subA
            __init__.py
            sa1.py
            sa2.py
        __init__.py
        a1.py
        a2.py
    packB/                 # package packB (implicit namespace package)
        b1.py
        b2.py
    math.py
    random.py
    other.py
    start.py
```

Note that we do not place a `__init__.py` file in our root `test/` folder.

---
## What is an `import`?

When a module is imported, Python runs all of the code in the module file. When a package is imported, Python runs all of the code in the package’s `__init__.py` file, if such a file exists. All of the objects defined in the module or the package’s `__init__.py` file are made available to the importer.

---
## Basics of the Python `import` and `sys.path`

According to Python documentation, here is how an `import` statement searches for the correct module or package to import:

> When a module named `spam` is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named `spam.py` in a list of directories given by the variable `sys.path`. `sys.path` is initialized from these locations:
> 
> -   The directory containing the input script (or the current directory when no file is specified).
> -   `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable PATH).
> -   The installation-dependent default.
> 
> After initialization, Python programs can modify `sys.path`. The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. _Source: Python [2](https://docs.python.org/2/tutorial/modules.html#the-module-search-path) and [3](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)_

Technically, Python’s documentation is incomplete. The interpreter will not only look for a _file_ (i.e., module) named `spam.py`, it will also look for a _folder_ (i.e., package) named `spam`. 

Also, **Python imports are case-sensitive.** `import Spam` is not the same as `import spam`.