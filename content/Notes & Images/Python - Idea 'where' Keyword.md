When calling a function for example `plot` it is better to write a long ass line of code then multiple lines with temporary variables, I don't like it, so i want to pass from this:
```python
plot(3*i*t, t)
```
to this:
```python
plot(f(t),t)
where:
	f(t) = 3*i*t
```

The main take on this idea, is that when reading the code you firstly read the function you want to use, then you need to read the inputs.
It' key that we ==highlight the main function used==, **we need to remove boilerplate code**, or at least hid it.