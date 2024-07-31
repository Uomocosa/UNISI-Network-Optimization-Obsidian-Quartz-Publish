
[Python Official Docs](https://docs.python.org/3/library/pprint.html)

```python
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
"""
[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']
"""
```

```python
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)
"""
[['spam', 'eggs', 'lumberjack',
 'knights', 'ni'],
 'spam', 'eggs', 'lumberjack', 'knights',
 'ni']
"""
```

```python
tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
... ('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)
"""
('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))
"""
```