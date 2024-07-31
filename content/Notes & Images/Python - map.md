
Original Sources:
- [Youtube by 'Real Python'](https://www.youtube.com/watch?v=powVeMYKCSw&list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr&index=3)
---

Used in this file:
- [[Python - Generators]]
- [[Python - lambda Functions]]
---
Typically you want to use the `map` function to convert one list, most likely a tuple to another tuple, using a function:

~ Ex.:
```python
a = (1,2,3,4,5)
b = map(lambda x: x**2, a)
#b = <map object at 0x...> #Generator
b = tuple(b)
#b = (1,4,9,14,25)
```

~Ex.:
```python
a = (1,2,3,4)
b = ("a","b","c","d")
c = tuple(map(lambda x, y: str(x)+str(y), a,b))
#c = ("1a","2b","3c","4d")
```
---
# Why not use a for loop
You can use a `for` loop, or a [[Python - List Comprehension|list comprehension]], to do the same thing, tho the `map` function is a more functional way.