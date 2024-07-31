
~ Es.: 
```
Python/
	+-- myPackage/
		+-- __init__.py
		+-- function.py
		+-- subpackage/
			+-- __init__.py
			+-- sub_function.py
```

---

**sub_function.py**
```python
import sys
old_path = sys.path
package_path = "C:\User\Uomocosa\Python"
sys.path.append(package_path)
#---
# All absolute imports from myPackage
import myPackage.subpackage
from myPackage.susubpackage.function import function
#---
sys.path.append(old_path)

# ------------------------------------------------------------------
# ------------------------------------------------------------------

def sub_function():
	print("Madonna calamita nella valle dei cazzi di ferro")
	function()
	
# ------------------------------------------------------------------
# ------------------------------------------------------------------

def Test():
	sub_function()

# ------------------------------------------------------------------
# ------------------------------------------------------------------

if __name__ == "__main__":
	Test()

```

---
**function.py**
```python
import sys
old_path = sys.path
package_path = "C:\User\Uomocosa\Python"
sys.path.append(package_path)
#---
# All absolute imports from myPackage
# None
#---
sys.path.append(old_path)

# ------------------------------------------------------------------
# ------------------------------------------------------------------

def funcion():
	print("Harry Potter and The", end = "")
	
# ------------------------------------------------------------------
# ------------------------------------------------------------------

def Test():
	funcion()

# ------------------------------------------------------------------
# ------------------------------------------------------------------

if __name__ == "__main__":
	Test()

```

---