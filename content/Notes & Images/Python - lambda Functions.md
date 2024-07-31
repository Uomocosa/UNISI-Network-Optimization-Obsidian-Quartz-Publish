
[Real Pyhton - Appropiate Uses of Lambda Expressions](https://realpython.com/python-lambda/#:~:text=Lambdas%20in%20Python%20tend%20to%20be%20the%20subject%20of%20controversies.%20Some%20of%20the%20arguments%20against%20lambdas%20in%20Python%20are%3A)

Example of a lambda function:
```python
is_major_than_5 = lambda x: x > 5
assert is_major_than_5(6) == True
assert is_major_than_5(1) == False
```

<br>

Lambda with if statement:
```python
is_between_1_and_10 = lambda x: True if (x > 1 and x < 10) else False
assert is_major_than_5(6) == True
assert is_major_than_5(-1) == False
```

<br>

# When NOT to use lambda functions:
Lambdas in Python tend to be the subject of controversies. Some of the arguments against lambdas in Python are:

-   Issues with readability
-   The imposition of a functional way of thinking
-   Heavy syntax with the `lambda` keyword