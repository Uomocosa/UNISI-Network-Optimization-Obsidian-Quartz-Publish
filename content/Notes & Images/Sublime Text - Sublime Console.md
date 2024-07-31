To show the console in Sublime Text, which is usefull for all developer work (such as package and plugin creation) and more, go to:<br>`Menu >> View >> Show Console` (usually: `Ctrl+Alt+\`)

---
#### Debug
The console can be used for debugging, or just run a command, take for example the script of a simple plugin:
```python
import sublime, sublime_plugin

class HelloWorldExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello World")
```

This code (or plugin) once its compiled will wirte **at the top of the file** the string "Hello World".
To run it, write on the console:
```python
view.run_command('hello_world_example')
```
The run_command method will run the class with that name, note that from the class name 3 things changed (between HelloWorldExampleCommand and hello_world_example)
1. The first letter is lower case.
2. All the upper case letters after the first are replaced with "_" + the corrisponding lower case letter.
3. The "_command" part is removed.

> This steps are not random, Sublime does this for all sub-classes the user creates, when he wants to run them
> [[All/Code/Git/0. Coding Practicies/Sublime Text - Naming Command Classes|Why did the class had the name "HelloWordExampleCommand" ?]]

