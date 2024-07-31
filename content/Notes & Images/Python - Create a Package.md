# Python Packages

> Il metodo che preferisco quando creo un pacchetto di moduli in python

> **Premessa**:
> Ogni file all'interno di un *Package* avrà tutte le funzioni divise in file diversi, ogni file avrà il nome della funzione che implementa.

---

Ogni *Package* avrà questa struttura:
```
myPackage/
+-- __init__.py
+-- function_1.py
+-- function_1.py
+-- subPackage/
	+-- __init__.py
	+-- sub_function_1.py
	+-- sub_function_2.py

```
---
~ Es.: File '** ____init____.py**'  (in myPackage):
```python
# Functions
from myPackage.function_1 import function_1
from myPackage.function_2 import function_2

# Sub-Packages
from myPackage import subPackage
```
~ Es.: File '** ____init____.py**'  (in subPackage):
```python
# Functions
from myPackage.subPackage.sub_function_1 import sub_function_1
from myPackage.subPackage.sub_function_2 import sub_function_2
```
---
~ Es.: File '**function_1.py**'  (in subPackage):
```python
def function_1():
	print("DIO CANE")

# ------- TESTIN' -------
def PrintTest():
	function_1()

# -----------------------
if __name__ == "__main__":
	print(f"\nTesting: {__file__}")
	PrintTest()
	print()
```
---
~ Es.: Utilizzo myPackage:
```python
import myPackage
myPackage.function_1()
>>> DIO CANE
myPackage.subPackage.sub_function_1()
>>> BESTIA DIO

# You can also do this
# NOT RECOMMENDED (losing information)
import myPackage.subPackage as new_name
new_name. sub_function_1()
```
---