
Original Sources:
- [Youtube by 'Tech with Tim'](https://www.youtube.com/watch?v=t5Bo1Je9EmE)
---

~ Ex.:
```python
import asyncio
import time

async def main():
	print("DIOCANE")
	#time.sleep(1)
	TASK1 = asyncio.create_task(foo(42))
	TASK2 = asyncio.create_task(fighter())
	print("---- Ended main() ----")
	await TASK1, TASK2


async def foo(integer):	
	await asyncio.sleep(1)
	print("DIOMOSTRO")


async def fighter():	
	print("PORCODIO")
	return


asyncio.run(main())
```

```python
#OUTPUT
>>> DIOCANE
>>> ---- Ended main() ----
>>> PORCODIO
>>> DIOMOSTRO
[Finished in 1.2s]
```
