
```python
import collections
Animal = collections.namedtuple('Animal',
	('Species', 'eats_meat', 'eats_vegetables'))

tiger = Animal(Species = 'Panthera tigris tigris',
	eats_meat = True, eats_vegetables = False)
tiger.Species
#>>> Panthera tigris tigris
```