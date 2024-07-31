Using [[Python - Frozen dataclass]]:
<br>

- The simplest immutable structure:
```python
from dataclasses import dataclass

@dataclass(frozen = True)
class simple_person:
	name: str
	surname: str
	ID: str
	hobbies: str = None #Optional Parameter

John = simple_person("John", "Carter", 102012)
```

<br>

- Structure with "laws" and an invisible parameter at declaration "immutable_metadata"
```python
from dataclasses import dataclass

add_new_field = object.__setattr__

@dataclass(frozen=True)
class immutable_metadata:
	metadata1
	metadata2

@dataclass(frozen=True)
class Immutable:
	a: int
	b: int
	
	def __post_init__(self):
		print(type(self.a))
		if self.a is int: raise Exception
		if self.b is int: raise Exception

		metadata = immutable_metadata("porva","p")

		add_new_field(self, "metadata", metadata)

imm = Immutable(1,2)
print(imm.a)
print(imm.metadata.metadata1)
print(imm.metadata.metadata2)
```