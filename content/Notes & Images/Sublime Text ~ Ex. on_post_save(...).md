[StackOverflow](https://stackoverflow.com/questions/43279931/perform-action-before-save-on-pre-save)

My implementation:
> prints "diocane" once the file is saved
```python
import sublime
import sublime_plugin
import inspect

class HelloWorldEventListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
    	print("diocane")
```