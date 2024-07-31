
Original Sources:
- [Youtube by 'Real Python'](https://www.youtube.com/watch?v=aysceqdGFw8&list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr&index=5)
---

Used in this file:
- [[Python - map]]
---

 ## Δttention:
 `multiprocessing.Pool().map()` does not accept [[Python - lambda Functions|lambda functions]]
 
---

## ~ Ex.:
```python
import multiprocessing

a = (1,2,3,4,5,6,7)

def mappiing(x):
	import time.sleep
	time.sleep(1)
	return x+1

pool = multiprocessing.Pool()
b = pool.map(mappiing,a) 
#Should take 7 seconds it takes WAY LESS, 
#because the map is beind executed 
#in parallel with multiple processes
```

<br>

#### Optional: How many processes are runned at the same time:
```python
import multiprocessing
pool = multiprocessing.Pool(processes = 4)
```

<br>

#### Optional: How may task can a process take before starting a new process
```python
import multiprocessing
pool = multiprocessing.Pool(maxtasksperchild = 10)
# A process (~es. process number 17403) does 10 task 
# (~es.: executes 10 mapping from start to end than)
# kills itself and a new process (~es.: 17408) starts
```
---
