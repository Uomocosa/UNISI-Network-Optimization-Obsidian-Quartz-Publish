# Inspect - File Name
> ###### **Riassunto:** 
> file name of caller function
> [Documentazione](https://docs.python.org/3/library/inspect.html)
-----

<br>

### Codice
```python 
import inspect
current_frame = inspect.currentframe()
call_frame = inspect.getouterframes(current_frame, 2)
print('caller frame:', call_frame[1][1])

>>> h:\Arduino_Codes\GDA_from_Builtin_Accelerometer_2\Python\D.py
```