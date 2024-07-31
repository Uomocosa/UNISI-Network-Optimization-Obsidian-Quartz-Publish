
Original Sources:
- [Youtube by 'Real Python'](https://www.youtube.com/watch?v=fkjjqyfN51c&list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr&index=2)
---

Used in this file:
- [[Python - lambda Functions]]
- [[Python - Generators]]
---

~ Ex.:
```python
a = (1,2,3,4,5,6,7)
b = filter(lambda x: x > 5, a)
#b = <filter object at 0x10a34354> #is a GENERATOR
b = tuple(b)
#b = (6,7)
```
---
# How about a for loop?
You can use `for` loops to do the same thing, **but**:
- `for`  is not functional.
- `for`  is more verbose.
- `filter` can chained and composed with other function really well