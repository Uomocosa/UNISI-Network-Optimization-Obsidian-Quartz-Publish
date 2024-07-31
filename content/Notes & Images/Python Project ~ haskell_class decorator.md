# Idea:
Once a class is created i want it to be immutable, but i dont want to re-write every time the "initial conditions", so i create a decorator that overwrites the \_\_setattr\_\_ function of a class, and adds an **update** function where it creates a copy of the class with only some of the fields changed

---
# Code:
```python
from dataclasses import dataclass
import copy

class Haskell_Class():
	def __init__(self):
		self.__haskell_class__ = True

	def __setattr__(self, name, value):
		try: 
			if self.__haskell_class__ == True: return
		except AttributeError: self.__dict__[name] = value


def freze_after_initialization(self, name, value):
	try: 
		if self.__haskell_class__ == True: return
	except AttributeError: self.__dict__[name] = value

def haskell_class(cls):
	def wrapper(*args, **kwargs):
		new_class_instance = cls(*args, **kwargs)
		new_class_instance.__haskell_class__ = True
		setattr(new_class_instance, "__setattr__", freze_after_initialization)
		return new_class_instance
	return wrapper


def is_haskell_class(cls):
	try: return cls.__haskell_class__
	except AttributeError: return False


def haskell_class(cls):
	def new_init(func):
		def wrapper(self, *args, **kwargs):
			func(self, *args, **kwargs)
			setattr(self, "__haskell_class__", True)
		return wrapper


	def freze_after_initialization(self, name, value):
		if is_haskell_class(self) and name != "__haskell_class__":
			if self.__haskell_class__ == True: 
				err_msg = "\n\tClass is defined as an HASKELL_CLASS"
				err_msg += "\n\tTo change a value use the function update(...)"
				raise AttributeError(err_msg)
		self.__dict__[name] = value


	def update(self, **kwargs):
		new_class_instance = copy.deepcopy(self)
		new_class_instance.__haskell_class__ = False
		for key in kwargs:
			if key not in new_class_instance.__dict__:
				err_msg = f"{key} is not an instance of the class"
				raise AttributeError(err_msg)
			new_class_instance.__dict__[key] = kwargs[key]
		new_class_instance.__haskell_class__ = True
		return new_class_instance


	cls.__init__ = new_init(cls.__init__)
	cls.__setattr__ = freze_after_initialization
	cls.update = update
	return cls



def Test():
	@haskell_class
	@dataclass
	class PORVA():
		a : int
		b : int

	print("START")
	a = Haskell_Class()
	b = PORVA(3, 4)
	print(b.a)
	print(b.update(a = 1, b = 3))
	print(b)

if __name__ == '__main__':
	Test()
```

