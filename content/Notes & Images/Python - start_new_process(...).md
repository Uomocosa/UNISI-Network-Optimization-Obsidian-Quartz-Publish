### Things to note:
- The `import __init__` is at the first line is due to how i write [[Python - HOW I IMPORT - My __init__.py Files|my inits]]
- Dont worry about all the functions and variables declared other than `start_new_process`, they will all be invisible to the end user; From the otehrs file you can call only see `start_new_process`, this is still due to how i write the \_\_init\_\_
- The class `immutable_process` is there for beauty at most, it can be easily removed from the code
- In the `Test()` function note how the total wait should be 6+seconds, but when running the code, it drops down to ~3.4s, because the functions runs in two different processes
- **IMPORTANT**: Do not pass `map` in any way to this processes, they will brake and not even report an error, just run indefinitely
<br>
```python
import __init__
import collections
import dill
import multiprocessing
import types

create_collection = collections.namedtuple('new_process',(
    'Queue', 'Process',))

class immutable_process(create_collection):
    queue_and_process: tuple

    def __init__(self, queue, process):
        self.queue_and_process = create_collection(queue, process)

    def __str__(self):
        msg = f"Queue = {self.queue_and_process.Queue}"
        msg += f"\nProcess = {self.queue_and_process.Process}"
        return msg

    def finish_process(self):
        if self.queue_and_process.Process.is_alive():
            self.queue_and_process.Process.join()
        return self.queue_and_process.Queue.get()

    def is_alive(self):
        return self.queue_and_process.Process.is_alive()

#IMPURE #cannot make it pure :(
def add_to_queue(queue, dumped_function, *args, **kwargs):
    loaded_function = dill.loads(dumped_function)
    results = loaded_function(*args, **kwargs)
    queue.put(results)
    return

def add_function_to_queue(queue, function, *args, **kwargs):
    results = function(*args, **kwargs)
    queue.put(results)
    return

def start_new_process(function, *args, **kwargs): # spawns child processes
    if function is map:
        raise TypeError("DO NOT pass map in any way to this function")
    q = multiprocessing.Queue()
    dumped_function = dill.dumps(function, recurse=True)
    process = multiprocessing.Process(
        target = add_to_queue, args = (q, dumped_function, *args, *kwargs))
    process.start()
    return immutable_process(q, process)


def Test():
	import time

    def useless_function1():
        time.sleep(3)

    q4 = start_new_process(useless_function1)
    
    uf2 = lambda x: useless_function1()
    my_sleep = lambda x: time.sleep(x)
    q5 = start_new_process(my_sleep,3)

    q4.finish_process()
    q5.finish_process()
	
	#THIS WILL FAIL
	q10 = start_new_process(map, lambda x: x + 2,(1,2,3,4))
	# The multiprocess.Process does NOT like the use of map
	
if __name__ == '__main__': Test()
    
```