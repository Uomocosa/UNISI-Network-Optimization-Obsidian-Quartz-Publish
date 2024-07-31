
Original Sources:
- [Youtube by 'Real Python']()
---

Used in this file:
- [[Python - lambda Functions]]
- [[Python - zip]]
- [[Python - List as Positional Args]]
---
Typical use: from **tuple_vectort** --> get **one_element**

~ Ex.:
```python
from functools import reduce
vector = (1,2,3,4,5)
element = reduce(lambda acc, val: acc - val, *vector)
element = -13 # ((((1-2)-3)-4)-5)
```

~ Ex.:
```python
from functools import reduce
def count(acc, val):
	if not acc.has_key(val):
		acc[val] = 1
	else:
		acc[val] += 1
	return acc
	
a = (1,2,1,2,3,4,1,2,3,5,6,3,2)
d = reduce(count, a, dict())
"""
d = {
	1: 3
	2: 4
	3: 3
	4: 1
	5: 1
	6: 1
}
"""
```
---
