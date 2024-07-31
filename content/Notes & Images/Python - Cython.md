- ***Source***: [Easy wins with Cython: fast and multi-core by Caleb Hattingh](https://www.youtube.com/watch?v=NfnMJMkhDoQ)
---
1. **Installation**: `pip install cython`
2. ***Write the cython file*** … it **MUST** end in `.pyx` 
   *~ex.:* `function.pyx`, 
   (*Instead of a normal python function file ~ex.: `function.py`*)
3. **Create a `setup.py` file with the following code**:
   ```python
   from setuptools import setup
   from Cython.Build import cythonize
   setup(
      ext_modules = cythonize('function.pyx')
   )
   ```
4. **Open the terminal end run the following command**:
   `python setup.py build_ext --inplace` 
5. It will build a binary file, somenthing like `function.cp39-win_amd64.pyd`, than **import it** normally with:
   ```python
   import function
   ```

This is the basic folder structure for this implementation
```
python package/
├── main.py
└── sub_package/
    ├── __init__.py
 	└──	src/
	 	├── cython_module.pyx
 		├── setup.py
 		├── cython_module.c
 		└── ...
```

---
### With my custom folder structuren (NOT WORKING)
```
python package/
├── main.py
└── sub_package/
    ├── __init__.py
    ├── cython_module.pyx
 	└──	src/
 		├── setup.py
 		├── cython_module.c
 		└── ...
```
- ***Objectives***:
	- I want to see only the `.pyx` files in my folder, all others files created need to be in the `src/` folder.
- ***Useful link***:
	- [Cython official docs](https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html)

**Code for the `setup.py` file**: #TODO 
```python
from setuptools import setup
from Cython.Build import cythonize
setup(
  ext_modules = cythonize('function.pyx')
)
```

**Command for the terminal**: #TODO 
```
python setup.py build_ext --inplace
```

---
