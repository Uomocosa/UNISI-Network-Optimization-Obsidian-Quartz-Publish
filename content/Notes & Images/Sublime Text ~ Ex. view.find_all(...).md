### From documentation:

**Method**: 
`
find_all(pattern, <flags>, <format>, <extractions>)
`

**Return Value**: 
[Region](https://www.sublimetext.com/docs/api_reference.html#sublime.Region)

**Description**:
Returns all (non-overlapping) regions matching the regex pattern. The optional flags parameter may be `sublime.LITERAL`, `sublime.IGNORECASE`, or the two ORed together. If a format string is given, then all matches will be formatted with the formatted string and placed into the extractions list.

---

~ Ex.:
```python
import sublime, sublime_plugin

class HelloWorldEventListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        print(view.find_all("s"))
```