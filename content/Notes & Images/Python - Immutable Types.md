
[Youtube by 'Real Python'](https://www.youtube.com/watch?v=xJCPpDlk9_w&list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr)

> Immutability: You can access the item and values it contains, but you **cannot** change them

In python if you want an immutable array, or list, u can use the *tuple*, or even if you want one single element to be immutable.
Immutable data have some [[Immutable data|interesting properties]].
```python
a = tuple((1,)) #IMMUTABLE ELEMENT
b = tuple((1,2,3)) #IMMUTABLE LIST
```

----

You can create any new type of immutable structure, or type using the [[Python - collections|collections module]]:
```python
#MUTABLE DATA EXAMPLE:
scientists = [
	{'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False}
	{'name': 'Emy Noether', 'field': 'math', 'born': 1882, 'nobel': False}
]
#And you can access it using:
first_scientis_name = scientists[0]['name']
```
```python
import collection
Scientist = collections.namedtuple('Scientist',
	('name', 'field', 'born', 'field'))
ada = Scientist(name = 'Ada Lovelace', 
	field = 'math', born = 1815, nobel = False)

#if you want to access data:
print(ada.name)
#>>> 'Ada Lovelace'

# COMPLEATLY IMMUTABLE LIST OF STRUCTURES
scientists = tuple((
	Scientist(name = 'Ada Lovelace', 
		field = 'math', born = 1815, nobel = False),
	Scientist(name = 'Emy Noether', 
		field = 'math', born = 1882, nobel = False),
))
```
