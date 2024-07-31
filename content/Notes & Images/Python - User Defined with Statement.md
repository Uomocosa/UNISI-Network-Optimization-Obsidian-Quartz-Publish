##### Original Sources:
- 

---
##### Used in this file:
- [[]]

---
###### ~ Ex.:
define a class with dunder methods `__enter__` and `__exit__`, the first will be called at the start of the `with` statement, and the last at the end.
```python
class A:
    def __enter__(self, code):
       print code

    def __exit__(..):
       pass
```

and then:
```python
with A():
   f()
   g()
```

---
