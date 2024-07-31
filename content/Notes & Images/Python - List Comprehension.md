

Original Sources:
- [W3Schools](https://www.w3schools.com/python/python_lists_comprehension.asp)
---

Used in this file:
- [[Python - Generators]]
---

~ Ex.:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  
```

Instead of doing:
```python
newlist = []  
for x in fruits:  
  if "a" in x:  
    newlist.append(x)  
```

a better way is:
```python
generator = x for x in fruits if "a" in x
newlist = list(generator)
```

---
# Prefer Generators
In the two examples before the last return a generator, usually prefered to a for loop.

---
# How about a filter?
I personally recommand using [[Python - filter|the filter function]] instead, it is more functional, the Python PEP-8 prefer the list comprehension.