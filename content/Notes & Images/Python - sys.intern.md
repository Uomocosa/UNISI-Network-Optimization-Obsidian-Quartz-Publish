[Original Source](https://medium.com/techtofreedom/string-interning-in-python-a-hidden-gem-that-makes-your-code-faster-9be71c7a5f3e)

# Interning Strings Explicitly To Speed Up Your Code

Python, as an elegant programming language, always opens a door for us. As to string interning, there is a built-in function that we can use to intern a string explicitly. It is the `intern()` function in the `sys` module.

Let’s see how it works by a simple example:

```python
import sys  
c = sys.intern('Y'*4097)  
d = sys.intern('Y'*4097)  
c is d  
True
```

own above, with the help of the `intern()` function, we can force Python to intern the strings no matter what the implicit rules are.

In practice, if we need to compare some long strings and the same value may appear many times, using the `intern()` function explicitly is a recommended way to speed up the string comparisons.

On the one hand, it can take advantage of the string interning mechanism in Python. On the other hand, it will not let us fall into the trap of complex rules.

---