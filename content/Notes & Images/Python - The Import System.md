- ***Source***: [Youtube](https://www.youtube.com/watch?v=MCs5OvhV9S4)
----
### David Beazley (PyCon2015) | Index
- [[#Part I : Basic Knowledge]]
- [[#Part II : Packages]]
- [[#Part III : _ _main _ _]]
- [[#Part IV : sys.path]]
- [[#Part V : Namespace Packages]]
- [[#Part VI : The Module]]
- [[#Part VII : The Module Reloaded]]
- [[#Part VIII : Import Hooks]]
- [[#Part IX : Path Hooks]]
- [[#Part X : Final Comments]]

---
### Part I : Basic Knowledge
![[Pasted image 20221222144856.png]]
![[Pasted image 20221222144914.png]]
![[Pasted image 20221222144949.png]]
![[Pasted image 20221222145006.png]]
![[Pasted image 20221222145038.png]]
![[Pasted image 20221222145053.png]]
![[Pasted image 20221222145122.png]]
![[Pasted image 20221222145138.png]]
![[Pasted image 20221222145157.png]]
![[Pasted image 20221222145212.png]]
![[Pasted image 20221222145239.png]]
![[Pasted image 20221222145350.png]]
![[Pasted image 20221222145420.png]]
![[Pasted image 20221222145440.png]]
![[Pasted image 20221222145522.png]]
![[Pasted image 20221222145546.png]]
![[Pasted image 20221222145607.png]]

---
### Part II : Packages
![[Pasted image 20221222145740.png]]
![[Pasted image 20221222145805.png]]
![[Pasted image 20221222145843.png]]
![[Pasted image 20221222145919.png]]
![[Pasted image 20221222150013.png]]
![[Pasted image 20221222150050.png]]
![[Pasted image 20221222150202.png]]
![[Pasted image 20221222150259.png]]
![[Pasted image 20221222150337.png]]
![[Pasted image 20221222150413.png]]
![[Pasted image 20221222150550.png]]
![[Pasted image 20221222150643.png]]
![[Pasted image 20221222150656.png]]
![[Pasted image 20221222150725.png]]
![[Pasted image 20221222150747.png]]
![[Pasted image 20221222150923.png]]
![[Pasted image 20221222151019.png]]
![[Pasted image 20221222151037.png]]
![[Pasted image 20221222151233.png]]
![[Pasted image 20221222151250.png]]
![[Pasted image 20221222151433.png]]
![[Pasted image 20221222151447.png]]
![[Pasted image 20221222151502.png]]
![[Pasted image 20221222151628.png]]
![[Pasted image 20221222151725.png]]
![[Pasted image 20221222151839.png]]

---
### Part III : \_\_main\_\_
![[Pasted image 20221222151911.png]]
![[Pasted image 20221222151926.png]]
![[Pasted image 20221222152021.png]]
![[Pasted image 20221222152225.png]]
![[Pasted image 20221222152251.png]]
![[Pasted image 20221222152330.png]]
![[Pasted image 20221222152354.png]]
![[Pasted image 20221222152457.png]]

---
### Part IV : sys.path
![[Pasted image 20221222152533.png]]
![[Pasted image 20221222152553.png]]
![[Pasted image 20221222152648.png]]
![[Pasted image 20221222152720.png]]
![[Pasted image 20221222152729.png]]
![[Pasted image 20221222152751.png]]
![[Pasted image 20221222152924.png]]
![[Pasted image 20221222153000.png]]
![[Pasted image 20221222153040.png]]
![[Pasted image 20221222153118.png]]
![[Pasted image 20221222153153.png]]
![[Pasted image 20221222153231.png]]
![[Pasted image 20221222153249.png]]
![[Pasted image 20221222153322.png]]
![[Pasted image 20221222153336.png]]
![[Pasted image 20221222153423.png]]
![[Pasted image 20221222153443.png]]
![[Pasted image 20221222153525.png]]
![[Pasted image 20221222153546.png]]
![[Pasted image 20221222153616.png]]
![[Pasted image 20221222153634.png]]
![[Pasted image 20221222153759.png]]
![[Pasted image 20221222153813.png]]
![[Pasted image 20221222153847.png]]
![[Pasted image 20221222155233.png]]
![[Pasted image 20221222161508.png]]
![[Pasted image 20221222161526.png]]
![[Pasted image 20221222161557.png]]
![[Pasted image 20221222161638.png]]

---
### Part V : Namespace Packages
![[Pasted image 20221222161701.png]]
![[Pasted image 20221222161712.png]]
![[Pasted image 20221222161752.png]]
![[Pasted image 20221222161820.png]]
![[Pasted image 20221222161839.png]]
![[Pasted image 20221222161910.png]]
![[Pasted image 20221222161925.png]]
![[Pasted image 20221222161936.png]]
![[Pasted image 20221222161954.png]]
![[Pasted image 20221222162005.png]]
![[Pasted image 20221222162045.png]]
![[Pasted image 20221222162057.png]]
![[Pasted image 20221222162121.png]]
![[Pasted image 20221222162150.png]]
![[Pasted image 20221222162210.png]]
![[Pasted image 20221222162220.png]]
![[Pasted image 20221222162235.png]]
![[Pasted image 20221222162258.png]]

---
### Part VI : The Module
![[Pasted image 20221222162324.png]]

> **NOTE**:
> A module is somenthing you can create on the fly:
```python
import types
mod = types.ModuleType('spam')
print(mod)
# >> <module 'spam'>
print(mod.__dict__)
# >> {'__name__': 'spam', '__spec__': None, '__doc__': None,  '__package__': None, '__loader__': None}
```

![[Pasted image 20221222162809.png]]
![[Pasted image 20221222162820.png]]
![[Pasted image 20221222162407.png]]
![[Pasted image 20221222162933.png]]
![[Pasted image 20221222163013.png]]
![[Pasted image 20221222163039.png]]
![[Pasted image 20221222163058.png]]
![[Pasted image 20221222163133.png]]
![[Pasted image 20221222163215.png]]
![[Pasted image 20221222163234.png]]
![[Pasted image 20221222163307.png]]
![[Pasted image 20221222163317.png]]
![[Pasted image 20221222163331.png]]
![[Pasted image 20221222163343.png]]
![[Pasted image 20221222163409.png]]
![[Pasted image 20221222163420.png]]
![[Pasted image 20221222163431.png]]
![[Pasted image 20221222163440.png]]
![[Pasted image 20221222163453.png]]
![[Pasted image 20221222163506.png]]
![[Pasted image 20221222163607.png]]
![[Pasted image 20221222163630.png]]
![[Pasted image 20221222163639.png]]
![[Pasted image 20221222163655.png]]
![[Pasted image 20221222163724.png]]
![[Pasted image 20221222163738.png]]
![[Pasted image 20221222163756.png]]
![[Pasted image 20221222163940.png]]

---
### Part VII : The Module Reloaded
![[Pasted image 20221222164006.png]]
![[Pasted image 20221222164016.png]]
![[Pasted image 20221222164037.png]]
![[Pasted image 20221222164051.png]]
![[Pasted image 20221222164114.png]]
![[Pasted image 20221222164130.png]]
![[Pasted image 20221222164144.png]]
![[Pasted image 20221222164154.png]]
![[Pasted image 20221222164217.png]]
![[Pasted image 20221222164242.png]]
![[Pasted image 20221222164259.png]]

---
### Part VIII : Import Hooks
![[Pasted image 20221222164312.png]]
![[Pasted image 20221222164324.png]]
![[Pasted image 20221222164339.png]]
![[Pasted image 20221222164356.png]]
![[Pasted image 20221222164433.png]]
![[Pasted image 20221222164452.png]]
![[Pasted image 20221222164526.png]]
![[Pasted image 20221222164554.png]]
![[Pasted image 20221222164736.png]]
![[Pasted image 20221224105422.png]]
![[Pasted image 20221224105514.png]]
![[Pasted image 20221224105551.png]]
![[Pasted image 20221224105628.png]]

> **NOTE**:
> You can “populate” a module you created with another module
```python
import types, socket
mod = types.ModuleType('my_socket')
print(mod.__dict__)
# >> {'__name__': 'my_socket', '__doc__': None,  '__package__': None, '__spec__': None, '__loader__': None}
print(socket.loader)
# >> <_forzen_importlib.SourceFileLoader ...>
socket.loader.exec_module(mod)
print(mod.__dict__)
# now the mod.__dict__ is almost identical to the socket.__dict__ except for value in the '__name__'
```

![[Pasted image 20221224110444.png]]
![[Pasted image 20221224110517.png]]
![[Pasted image 20221224110529.png]]
![[Pasted image 20221224110558.png]]
![[Pasted image 20221224110700.png]]
![[Pasted image 20221224110731.png]]
![[Pasted image 20221224110814.png]]
![[Pasted image 20221224110828.png]]
![[Pasted image 20221224111050.png]]
![[Pasted image 20221224111156.png]]
![[Pasted image 20221224111135.png]]
![[Pasted image 20221224111226.png]]
![[Pasted image 20221224111336.png]]
![[Pasted image 20221224111422.png]]
![[Pasted image 20221224111611.png]]
![[Pasted image 20221224111714.png]]
![[Pasted image 20221224111737.png]]

---
### Part IX : Path Hooks
![[Pasted image 20221224111806.png]]
![[Pasted image 20221224111825.png]]
![[Pasted image 20221224111917.png]]
![[Pasted image 20221224112213.png]]
![[Pasted image 20221224112228.png]]
![[Pasted image 20221224112318.png]]
![[Pasted image 20221224112420.png]]
![[Pasted image 20221224112437.png]]
![[Pasted image 20221224112458.png]]
![[Pasted image 20221224112731.png]]
![[Pasted image 20221224112815.png]]
![[Pasted image 20221224113036.png]]
![[Pasted image 20221224113058.png]]

---
### Part X : Final Comments
![[Pasted image 20221224113120.png]]
![[Pasted image 20221224113135.png]]
![[Pasted image 20221224113221.png]]
![[Pasted image 20221224113243.png]]
![[Pasted image 20221224113309.png]]


---
# Online Resources:

THE BEST video on the topic i could find: [Youtube by 'Sreekanth'](https://www.youtube.com/watch?v=QCSz0j8tGmI&t=776s)
- Its references:
		- [Python Official Docs: The import system](https://www.youtube.com/watch?v=Zz-7b_eBpz0)
		- [Python Official Docs: Modules](https://docs.python.org/3/tutorial/modules.html)
		- [Python Official Docs: The implementation of `import`](https://docs.python.org/3/library/importlib.html)
		- [Pep 420](https://www.python.org/dev/peps/pep-0420/)
		- [Youtube by 'PyCon 2015'](https://www.youtube.com/watch?v=0oTh1CXRaQ0)