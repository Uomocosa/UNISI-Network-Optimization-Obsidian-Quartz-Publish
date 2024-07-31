
Original Sources:
- [Youtube by 'Sreekanth']()
---

Used in this file:
- [[Python - Color Output]]
---

~ Ex.:
```python
class Frob:
	def __init__(self, bamf):
		self.bamf = bamf

	def __getattr__(self, name):
		return 'Frob does not have `{}` attribute.'.format(str(name))


f = Frob("boo")
print(f.bar)
>> "Frob does not have `bar` attribute."
print(f.bamf)
>> "boo"
```
---
# Change how the "." works
Normally if i typed `f.bar`  it would return an error in this case i changed the behaviour.