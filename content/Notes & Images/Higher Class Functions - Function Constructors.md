Those function that create other functions, such as:
```python
def create_specific_sum(x)
	def sum (y):
		return x + y
		
	return sum

sum_3_to = create_specific_sum(3)
assert sum_3_to(4) == 7
```

<br>

In python and other languages, it can be generalized from a [[First Order Functions]] using the [partial](https://docs.python.org/3/library/functools.html) function:
```python
from functools import partial

def sum(x, y):
	return x + y

sum_3_to = partial(sum, x = 2)

assert sum_3_to(1) == 4
```

