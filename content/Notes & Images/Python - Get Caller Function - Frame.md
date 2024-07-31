# Inspect - Frame
> ###### **Riassunto:** 
> frame object at this level
> [Documentazione](https://docs.python.org/3/library/inspect.html)
-----

<br>

### Codice
```python 
import inspect
current_frame = inspect.currentframe()
call_frame = inspect.getouterframes(current_frame, 2)
print('caller frame:', call_frame[1][0])

>>> <frame object at 0x03543510>
```

> *Cos'è un Frame?*
> [[Python - Frame]]
