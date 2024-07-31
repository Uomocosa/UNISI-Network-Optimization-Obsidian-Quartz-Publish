
[YouTube: 'What Does It Take To Be An Expert At Python?' by 'Coding Tech'](https://www.youtube.com/watch?v=7lmCu8wz8ro)

---
A generators is a function that does not use `return` but instead the keyword `yield`.
```python
def my_range(a, b, i = 0):
	if i >= (b - a):
		yield i + a
		i += 1
		my_range(a, b, i):
```

<br>

The `yield` keyword stop the execution until the keyword `next` is called on that iterator
```python
r = my_range(1,3)
# r = <iterator object at 0x23321h334>
next(r)
# 1
next(r)
# 2
next(r)
# StopIteration Exeption
```