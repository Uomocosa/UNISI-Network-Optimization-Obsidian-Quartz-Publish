
Original Sources:
- [StackOverflow](https://stackoverflow.com/questions/5929107/decorators-with-parameters#:~:text=def%20decorator(argument)%3A%0A%20%20%20%20def%20real_decorator(function)%3A%0A%20%20%20%20%20%20%20%20def,argument%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20result%0A%20%20%20%20%20%20%20%20return%20wrapper%0A%20%20%20%20return%20real_decorator)
---

Used in this file:
- [[Python - Decorators]]
---

~ Ex.: Declaration
```python
def decorator(argument):
    def real_decorator(function):
        def wrapper(*args):
            for arg in args:
                assert type(arg)==int,f'{arg} is not an interger'
            result = function(*args)
            result = result*argument
            return result
        return wrapper
    return real_decorator
```
~Ex.: Usage of the decorator:
```python
@decorator(2)
def adder(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
```
~Es.: Use of the function:
```python
adder(2,3) #Returns 10
adder('hi',3) #Returns AssertionError
```
---
