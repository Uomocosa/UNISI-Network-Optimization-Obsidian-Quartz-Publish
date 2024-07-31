
If a class has been declared for example as:
```python 
class GenericNameOfAClassCommand(sublime_plugin.TextCommand)
```

or as:
```python 
class AnotherNameHandler(sublime_plugin.InputHandler)
```

<br>

Then when refering to the class in the same package folder, such as in another "**.py**" extension the name is the same.
**BUT** when refering to this classes in a "**[[Sublime Text - Package Resources or sublime-extensions|.sublime-extension]]**" or in the [[Sublime Text - Sublime Console|console]] than the name changes.

> For the `GenericNameOfAClassCommand` class the name becomes `generic_name_of_a_Class`

> And for `AnotherNameHandler` it becomes `another_name`


The general protocol is:
1. The first letter is lower case.
2. All the upper case letters after the first are replaced with "_" + the corrisponding lower case letter.
3. If there is a "_command" part at the end, or a "_handler" part, then it is removed.
