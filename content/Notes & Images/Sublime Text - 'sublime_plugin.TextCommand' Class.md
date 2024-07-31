##### Original Sources:
- [Youtube by 'OdatNurd'](https://youtu.be/N65RwYb32vI?t=151)
- [Sublime Text API](https://www.sublimetext.com/docs/api_reference.html#:~:text=sublime_plugin.TextCommand%20Class,via%20self.view)

---
##### Used in this file:
- [[Sublime Text - All sublime.view Methods]]

---
###### ~ Ex.:
```python
import sublime, sublime_plugin

class ExampleOneCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
```

---
# Remeber:
Pass `edit` to the `run` function as argument only if you intend to modify the `view`
