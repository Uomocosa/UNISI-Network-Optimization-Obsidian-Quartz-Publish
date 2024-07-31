# Inspect - Line Number
> ###### **Riassunto:** 
> current line number in Python source code
> [Documentazione](https://docs.python.org/3/library/inspect.html)
-----

<br>

### Codice
```python 
import inspect
current_frame = inspect.currentframe()
call_frame = inspect.getouterframes(current_frame, 2)
print('caller frame:', call_frame[1][2])

>>> 51
```