
Original Sources:
- [Real Python](https://realpython.com/python-gil/)
---
# What is it?
The Python Global Interpreter Lock or [GIL](https://wiki.python.org/moin/GlobalInterpreterLock), in simple words, is a mutex (or a lock) that allows only one [thread](https://realpython.com/intro-to-python-threading/) to hold the control of the Python interpreter.

<br>

## What Problem Did the GIL Solve for Python?
Python uses reference counting for [memory management](https://realpython.com/python-memory-management/). It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory occupied by the object is released.

The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously. If this happens, it can cause either leaked memory that is never released or, even worse, incorrectly release the memory while a reference to that object still exists. This can cause crashes or other “weird” bugs in your Python programs.

<br>

## How to Deal With Python’s GIL
If the GIL is causing you problems, here a few approaches you can try:

**Multi-processing vs multi-threading:** The most popular way is to use a multi-processing approach where you use multiple processes instead of threads. Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem. Python has a [`multiprocessing`](https://docs.python.org/2/library/multiprocessing.html) module which lets us create processes easily like this:
```python
from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
```
```python
# Time taken in seconds - 4.060242414474487
```