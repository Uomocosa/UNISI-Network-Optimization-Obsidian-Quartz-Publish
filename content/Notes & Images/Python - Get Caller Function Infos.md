# Inspect - currentframe
> ###### **Riassunto:** 
> Ricevi tutte le informazioni che potresti desiderare sulla funzione chiamante
-----
<br>

### Utilizzo
```python 
import inspect
current_frame = inspect.currentframe()
call_frame = inspect.getouterframes(current_frame, 2)
print('caller name:', call_frame[1][2])
```

Per utilizzi più avanzati:
- [[Python - Get Caller Function - Frame]]
- [[Python - Get Caller Function - File Name]]
- [[Python - Get Caller Function - Calling Line Number]]
- [[Python - Get Caller Function - Name]]
- [[Python - Get Caller Function - Next Inner Traceback Object]]
