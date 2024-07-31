
Given an input **x** to a function *f* the result *f(* **x** *)* will **NEVER** produce [[Side Effects]], or more abstractly, will not influence the outside world.

```python
//Example of a pure function
def add(x, y):
	return x + y
```
<br>

```python
//Example of a NON-pure function
def add_element_to_list(list, element):
	return list.append(element)
```
List changes state, because of the append function
Before function call `list = [1,2,3]`
After function call `list = [1,2,3,4]`
<br>

```python
//Make it PURE
def add_element_to_list(list, element):
	return list + [element]
```
Before function call `list = [1,2,3]`
After function call `list = [1,2,3]`
