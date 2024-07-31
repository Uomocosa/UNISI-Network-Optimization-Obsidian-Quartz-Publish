
If the class you want to run is a [[Sublime Text - 'sublime_plugin.TextCommand' Class|command class]] then write in the [[Sublime Text - Sublime Console|console]]: `view.run_command('name_of_the_class')`

> **NOTE**:
> The name_of_the_class [[Sublime Text - Class Name Protocol|is a little different]] than how you declared it. 

---
### Alternately:
If u want to run it in the plugin and not by the console (or bind it to a key):
```pyhton
sublime.active_window().run_command("name_of_the_class")
```

> **NOTE**:
> This works both for `sublime.WindowCommand` sub-classes and `sublime.TextCommand` sub-classes.
> The only difference is that when using a text command the command gets run for each loading of the plugin, while the window command gets run for the first and only time when the window becomes active and the plugin is loaded.
