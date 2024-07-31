Using [[Python - Frozen dataclass]]:

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
	
	def print_values(slef): print(f"a = {a}, b = {b}")
		

imm = Immutable(1,2)
print(imm.a)
print(imm.sum)
print(imm.sub)
imm.print_values()
```