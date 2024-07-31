[Python Documentation](https://docs.python.org/3/library/functools.html#:~:text=functools.partial(func%2C%20/%2C%20*args%2C%20**keywords)%C2%B6)

~ Ex.:
```python
from functools import partial

def sum(x, y):
    return x + y

sum_3_to = partial(sum, x = 2)

assert sum_3_to(1) == 4
```