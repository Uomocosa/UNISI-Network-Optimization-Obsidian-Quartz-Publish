
Used in this file:
- [[]]
---

~ Ex.:
```python
class do_somenthing():
	state_a = ""
	state_b = 10

	def __new__(cls, input_1, input_2 = None):
		print(input_1)
		print(input_2)
		return state_b + input_1

print(do_somenting(1))
>>> 11
```
---
# Intuition
The idea is to create encapsulated function that bring with them a state, these are to be considered the **MOST impure** function in the code, and when possible to be used the least amount of time, and only at the end of a project

The basic use of these class-functions is the moment you think you would **need a global variable** to be used in your function.

> If more function need the same shared state, then it's best to use a normal class, or (preferably) an haskell-class, where the state is immutable.

An useful concept to be associated with these class-function is the Singleton.
One example could be 'Count the number of times this function is being used'.