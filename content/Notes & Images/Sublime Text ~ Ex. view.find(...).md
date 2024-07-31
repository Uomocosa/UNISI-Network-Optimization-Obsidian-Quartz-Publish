### From documentation:

**Method**: 
`find(pattern, start_point, <flags>)`

**Return Value**: 
[Region](https://www.sublimetext.com/docs/api_reference.html#sublime.Region)

**Description**:
Returns the first region matching the regex pattern, starting from start_point, or `Region(-1, -1)` if it can't be found. The optional flags parameter may be `sublime.LITERAL`, `sublime.IGNORECASE`, or the two ORed together.

---

~ Ex.:
```python
import sublime, sublime_plugin
class AfterSavingEventListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        print(view.find("s", 0))
```