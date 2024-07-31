
I suggest you create a new folder [[Sublime Text - Package Folder|at this path]] called as you wish, and then create this file there.
> [[Sublime Text - Run a General Command|How to run this file]]

```python
import sublime, sublime_plugin

class HelloWorldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello World")
		
#TO RUN THIS FILE:
#	1.Open the Console
#	2.Digit: `view.run_command('hello_world')`
```