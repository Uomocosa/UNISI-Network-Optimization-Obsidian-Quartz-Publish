[StackOverflow](https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function)

```python
def get_precedent_variable_name_of_argument(argument):
    lcls = inspect.stack()[2][0].f_locals
    for name in lcls:
        if id(argument) == id(lcls[name]): return name
    return None
```