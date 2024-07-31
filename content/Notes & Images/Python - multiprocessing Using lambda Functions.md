
Original Sources:
- [StackOverflow - dump and load](https://stackoverflow.com/questions/19984152/what-can-multiprocessing-and-dill-do-together#:~:text=import%20multiprocessing%20as%20mp%0Aimport%20dill%0Adef,return%20%5Bf.get()%20for%20f%20in%20futures%5D)
- [StackOverflow - dump with 'recurse'](https://stackoverflow.com/questions/45616584/serializing-an-object-in-main-with-pickle-or-dill#:~:text=import%20time%0Aimport%20dill%0A%0Adef%20my_func(a%2C%20b)%3A%0A%20%20time.sleep(0.1)%0A%20%20return%20a%20%2B%20b%0A%0Awith%20open(%22tmp.pkl%22%2C%20%22wb%22)%20as%20f%3A%0A%20%20dill.dump(my_func%2C%20f%2C%20recurse%3DTrue))
- [StackOverflow - if you want to use cPickle](https://stackoverflow.com/questions/16626429/python-cpickle-pickling-lambda-functions#:~:text=import%20cPickle%20as%20pickle%0Afrom%20numpy%20import%20sin%2C%20cos%2C%20array%0Adef%20tmp(x)%3A%0A%20%20%20%20return%20sin(x)%2Bcos(x)%0Atest%20%3D%20array(%5B%5Btmp%2Ctmp%5D%2C%5Btmp%2Ctmp%5D%5D%2Cdtype%3Dobject)%0Apickle.dump(%20test%2C%20open(%27test.lambda%27%2C%27w%27)%20))
- [Code Redirect - if you want to use PiCloud](https://coderedirect.com/questions/290958/python-pickling-nested-functions#:~:text=PiCloud%2Dserialized%20objects%20can%20be%20de%2Dserialized%20using%20the%20normal%20pickle/cPickle%20load%20and%20loads%20functions.)
- [Program Creek - 'dill' code examples](https://www.programcreek.com/python/example/95968/dill.dump)
- ['dill' documentation](https://dill.readthedocs.io/en/latest/dill.html)
---

Used in this file:
- [[Python - lambda Functions]]
- [[Python - multiprocessing]]
---

~ Ex.:
```python
import multiprocessing as mp
import dill
def helperFunction(f, inp, *args, **kwargs):
    import dill # reimport, just in case this is not available on the new processes
    f = dill.loads(f) # converts bytes to (potentially lambda) function
    return f(inp, *args, **kwargs)
def mapStuff(f, inputs, *args, **kwargs):
    pool = mp.Pool(6) # create a 6-worker pool
    f = dill.dumps(f, recurse=True) # converts (potentially lambda) function to bytes
    futures = [pool.apply_async(helperFunction, [f, inp, *args], kwargs) for inp in inputs]
    return [f.get() for f in futures]
	
if __name__ == "__main__":
	mapStuff(lambda x: x**2, [2, 3]) # returns [4, 9]
	mapStuff(lambda x, b: x**2 + b, [2, 3], 1) # returns [5, 10]
	mapStuff(lambda x, b: x**2 + b, [2, 3], b=1) # also returns [5, 10]
	def f(x):
		return x**2
	mapStuff(f, [4, 5]) # returns [16, 25]
```
---
# Look at me Pickle is a bitch
The pickle module used to create a multiprocess code, or programm does not allow in any way the use of lambda functions, insted of normal ones, not only that it does not even allow nested functions to be passed around.
This is bullshit.
So we can use the **dill** module (not standard library) to dump the function, even a lambda one or nested functions and than load it again to be used in the **multiprocess** module.