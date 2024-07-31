

Original Sources:
- [PY4U.net - all kind of approches'](https://www.py4u.net/discuss/147107)
- [StackOverflow - Process and Queue](https://stackoverflow.com/questions/35943822/how-do-i-retrieve-output-from-multiprocessing-in-python/35944315#:~:text=if%20__name__%20%3D%3D%20%27__main__%27%0A%20%20%20%20q,ready%0A%20%20%20%20%23%20Process%20my%20output)
---

Used in this file:
- [[Python - Color Output]]
---

~ Ex.:
```

```
---
# Different Approaches:
Searching online you cannot find one easy solution, but you can find some approaches tho every one has at the core the same idea to make it work, parallel code, one that assume the role of a timer (and master code) and the other that runs the function (slave code), if the timer espiers, kill the slave code and raise a **TimeoutError**, if the function finishes before the timer espiers, kill the timer code and continue normally.
> The "timeout function" is really useful if I want to decide at run time between two algorithms such as one is faster for small iterations, and the other faster for really long ones.

So the approaches i found on internet are:
- Using threads (tho killing a thread is consider **bad practice**)
- Using asyncio (but once a process is started it has to end, so cannot use this approach for what i have in mind)
- Using multiprocessing (really good, and i took it a step further: [[Python - start_new_process(...)]])