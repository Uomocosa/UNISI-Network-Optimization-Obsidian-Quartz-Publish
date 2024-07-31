##### Original Sources:
- [Sublime Text API](https://www.sublimetext.com/docs/api_reference.html#:~:text=sublime_plugin.WindowCommandClass,via%20self.window)

---
##### Used in this file:
- [[Sublime Text - All sublime.window Methods]]

---
###### ~ Ex.:
```python
import sublime, sublime_plugin

class ExampleOneCommand(sublime_plugin.WindowCommand):
	def run(self, edit):
		active_sheet = self.window.active_sheet()
		active_view = self.window.active_view()
```

---
# Remeber:
Pass `edit` to the `run` function as argument only if you intend to modify the `window`