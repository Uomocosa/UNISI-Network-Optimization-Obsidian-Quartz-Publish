# Inspect - Function Name
> ###### **Riassunto:** 
> caller function name
> [Documentazione](https://docs.python.org/3/library/inspect.html)
-----

<br>

### Codice
```python 
import inspect
current_frame = inspect.currentframe()
call_frame = inspect.getouterframes(current_frame, 2)
print('caller frame:', call_frame[1][3])

>>> foo
```