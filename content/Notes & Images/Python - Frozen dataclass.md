An easy way to make an [[Python - Immutable Class|immutable class]], or [[Python - Immutable Struct|immutable struct]]

```python
from dataclasses import dataclass

# Substitute this line of code 
add_new_field = object.__setattr__
""" with
from myPackage.Immutable.frozen_dataclass import add_new_field
# myPackage.Immutable.frozen_dataclass.add_new_field
"""

@dataclass(frozen=True)
class Immutable:
	a: int
	b: int
	
	def __post_init__(self):
		print(type(self.a))
		if self.a is int: raise Exception
		if self.b is int: raise Exception

		sum = self.a + self.b
		sub = self.a - self.b

		add_new_field(self, "sum", sum)
		add_new_field(self, "sub", sub)


imm = Immutable(1,2)
print(imm.a)
print(imm.sum)
print(imm.sub)
```