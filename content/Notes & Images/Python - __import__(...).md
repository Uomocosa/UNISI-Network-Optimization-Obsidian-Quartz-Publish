[Official Documentation](https://docs.python.org/3/library/functions.html#:~:text=Note%20This%20is%20an%20advanced%20function%20that%20is%20not%20needed%20in%20everyday%20Python%20programming%2C%20unlike)

---

For example, the statement `import spam` results in bytecode resembling the following code:

```python
spam = __import__('spam', globals(), locals(), [], 0)
```

---

The statement `import spam.ham` results in this call:

```python
spam = __import__('spam.ham', globals(), locals(), [], 0)
```

---

Note how [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") returns the toplevel module here because this is the object that is bound to a name by the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement.

On the other hand, the statement `from spam.ham import eggs, sausage as saus` results in:
```python
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage
```
---
I like to use it in combo with `globals()`, `locals()` and `getattr()`, doing so i can generalize the import metod using strings:
```python
import Package.function
Package.function = Package.function.function
#I usually declare only one function with the same 
#name of the file 
#ITS EQUAL OF DOING:
locals()['Package.function'] = __import__(
	'Package.function',
	globals(),
	locals(),
	['function'],
	0,
)
locals()['Package.function'] = getattr(
	locals()['Package.function'],
	'function'
)
```