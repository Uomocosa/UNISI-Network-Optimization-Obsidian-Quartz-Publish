From [Sublime API Reference](https://www.sublimetext.com/docs/api_reference.html): "*Packages/Default/mark.py*"
- Uses add_regions( ) to add an icon to the gutter

<br>

```python
import sublime
import sublime_plugin


class SetMarkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        mark = [s for s in self.view.sel()]
        self.view.add_regions("mark", mark, "mark", "dot", sublime.HIDDEN | sublime.PERSISTENT)


class SwapWithMarkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        old_mark = self.view.get_regions("mark")

        mark = [s for s in self.view.sel()]
        self.view.add_regions("mark", mark, "mark", "dot", sublime.HIDDEN | sublime.PERSISTENT)

        if len(old_mark):
            self.view.sel().clear()
            for r in old_mark:
                self.view.sel().add(r)


class SelectToMarkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        mark = self.view.get_regions("mark")

        num = min(len(mark), len(self.view.sel()))

        regions = []
        for i in range(num):
            regions.append(self.view.sel()[i].cover(mark[i]))

        for i in range(num, len(self.view.sel())):
            regions.append(self.view.sel()[i])

        self.view.sel().clear()
        for r in regions:
            self.view.sel().add(r)


class DeleteToMark(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("select_to_mark")
        self.view.run_command("add_to_kill_ring", {"forward": False})
        self.view.run_command("left_delete")
```