
[Youtube by 'Real Python']()

Why use immutable data:
- If you want to have a multi-threaded program, do some parallel processing, you dont have to worry about locking the data stucture, because there was no way to update it.
- Never worry about changing the **state** of a structure.
- If you use immutable data stucture, a lot of time leads to a cleaner conceptual model.
- Easy to come up with an history of the calculation made.