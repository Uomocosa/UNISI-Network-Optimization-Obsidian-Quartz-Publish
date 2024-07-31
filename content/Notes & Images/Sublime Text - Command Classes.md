In a [[Sublime Text - Sublime Plugins|sublime plugin]] we define a subclass of a **Command** class, or better a "**command sub-class**", when we want to define a command or function using the sublime API, for example when we want to use the view methods
- [[Sublime Text - 'sublime_plugin.TextCommand' Class|sublime_plugin.TextCommand]]
- [[Sublime Text - 'sublime_plugin.WindowCommand' Class|sublime_plugin.WindowCommand]]
- [[Sublime Text - 'sublime_plugin.ApplicationCommand' Class]]

The differences between the two is only when they are defined in the "timeline":
- The `sublime_plugin.TextCommand` classes are instantiated once per view. The View object may be retrieved via `self.view`
- The `sublime_plugin.WindowCommand` classes are instantiated once per window. The Window object may be retrieved via `self.window`
- The `sublime_plugin.ApplicationCommand` classes.