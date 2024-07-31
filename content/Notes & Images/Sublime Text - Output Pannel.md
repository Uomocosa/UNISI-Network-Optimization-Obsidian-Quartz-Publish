***Source***: [Sublime Forum](https://forum.sublimetext.com/t/how-do-i-use-this-feature/58251)
```python
panel = window.create_output_panel('Test') 
panel.run_command('insert', {'characters': 'I am the contents of the test panel'})
window.run_command('show_panel', {'panel': 'output.Test'})
```

- As of right now (2024) there is still no way to **RESIZE** the console size via the API:<br>***Source***: [GitHub](https://github.com/sublimehq/sublime_text/issues/3601)<br>***Source***: [Forum](https://forum.sublimetext.com/t/style-the-output-panel/10316/10)
- **However**, Sublime will remember the height of the window if you change it manually.

----
###### More Context:
File: `pipenv.sublime-build` (insde the [[Sublime Text - User Folder|User folder]])
```json
{
    // This refers to the class TargetCommandPipenvBuild 
    // inside a file in the User folder
    "target": "target_command_pipenv_build", 
    
    "cmd": ["python", "-u", "$file"],
    "selector": "source.python",
}
```

File: `target_command_pipenv_build.py` (insde the [[Sublime Text - User Folder|User folder]])
```python
import sublime
import sublime_plugin
import subprocess


class TargetCommandPipenvBuild(sublime_plugin.WindowCommand):
    def run(self, cmd, **kwargs):
        window = sublime.active_window()
        porva_panel_View = window.create_output_panel("porva")
        porva_panel_View.run_command('insert', {'characters': 'This is a porva'})
        window.run_command('show_panel', {'panel': 'output.porva'})
```

File: `porva.py` (located wherever)
```python
print("Whatever")
```

Build it with the build system `pipenv`:
1. `Menu >> Tools >> Build System >> pipenv`
2. `Menu >> Tools >> Build` (usually `Ctrl+B`)
3. The output will be the *Output Panel*, on which it will be written: `This is a porva`

- ***Sources***:
	- [Official API](https://www.sublimetext.com/docs/api_reference.html#sublime.Window.create_output_panel)

----
# Index
- ***Source***: [Meta LLama 3 - online](https://www.llama2.ai)
- [[#In sublime text how is the space where the build result displaied called?]]
- [[#How can I print text in the "Output Pannel" from my plugin?]]
- [[#In the Sublime Text 4 API there is this "create_output_panel" function, how do I use it, make some examples?]]
- [[#In the Sublime Text 4 API there is this "create_output_panel" function, how do I use it, make some examples, in the context of the sublime_plugin.WindowCommand class]]
- [[#In Sublime Text 4 how can i Show Build Results, using my own target plugin?]]
- [[#]]

----
###### In sublime text how is the space where the build result displaied called?
(🦙 `From: LLama 3 • 70B`)

In Sublime Text, the space where the build result is displayed is called the "***Output Panel***".

---
###### How can I print text in the "Output Pannel" from my plugin?
(🦙 `From: LLama 3 • 70B`)

To print text in the "***Output Panel***" from your Sublime Text plugin, you can use the `window.run_command()` method and pass the `append` command with the `output_panel` argument.
Here's an example:
```python
import sublime
def plugin_function(window):
# Your plugin code here
message = "Hello, world!"
window.run_command("append", {"characters": message, "scope": "output_panel"})
```
This will append the text "Hello, world!" to the Output Panel.
If you want to clear the Output Panel before printing the text, you can use the `window.run_command()` method with the `erase` command:
```python
window.run_command("erase", {"scope": "output_panel"})
```
Then, you can append the text as shown above.
Note that `window` is an instance of the `sublime.Window` class, which represents the current Sublime Text window. You can get the current window using `sublime.active_window()` or by passing the `window` object as an argument to your plugin function.
Also, make sure to check the Sublime Text API documentation for more information on the available commands and their arguments.

---
###### In the Sublime Text 4 API there is this "create_output_panel" function, how do I use it, make some examples?
(🦙 `From: LLama 3 • 70B`)

The `create_output_panel` function in the Sublime Text 4 API is used to create a new output panel in the Sublime Text window. An output panel is a special type of view that is used to display output from plugins, such as the results of a build or the output of a command.
Here is a basic example of how to use the `create_output_panel` function:
```python
import sublime
import sublime_plugin
class ExampleCommand(sublime_plugin.TextCommand):
def run(self, edit):
panel = self.view.window().create_output_panel("example")
panel.insert(edit, panel.size(), "Hello, World!")
```
In this example, we create a new command called `ExampleCommand` that inserts the text "Hello, World!" into a new output panel when it is run.
Here's a breakdown of what's happening:
* `self.view.window().create_output_panel("example")`: This creates a new output panel with the name "example". The name is used to identify the panel, and it can be used to show or hide the panel later.
* `panel.insert(edit, panel.size(), "Hello, World!")`: This inserts the text "Hello, World!" into the output panel at the current cursor position (which is the end of the file, since we're inserting at `panel.size()`).
You can also use the `show` method to show the output panel after it's been created:
```python
panel = self.view.window().create_output_panel("example")
panel.insert(edit, panel.size(), "Hello, World!")
self.view.window().run_command("show_panel", {"panel": "output.example"})
```
This will show the output panel and make it visible to the user.
You can also use the `find_output_panel` method to retrieve an existing output panel:
```python
panel = self.view.window().find_output_panel("example")
if panel:
panel.insert(edit, panel.size(), "Hello, World!")
else:
print("Output panel not found")
```
This will insert the text "Hello, World!" into the existing output panel with the name "example", or print an error message if the panel doesn't exist.
I hope this helps! Let me know if you have any questions or need further examples.

----
###### In the Sublime Text 4 API there is this "create_output_panel" function, how do I use it, make some examples, in the context of the sublime_plugin.WindowCommand class
(🦙 `From: LLama 3 • 70B`)

The `create_output_panel` function in Sublime Text 4 API is used to create a new output panel in the active window. Here's how you can use it in the context of the `sublime_plugin.WindowCommand` class:
**Basic Example**
```python
import sublime
import sublime_plugin
class CreateOutputPanelCommand(sublime_plugin.WindowCommand):
def run(self):
panel = self.window.create_output_panel("my_panel")
panel.run_command("insert", {"characters": "This is an output panel!"})
```
In this example, when you run the `CreateOutputPanelCommand` command, it will create a new output panel named "my_panel" in the active window and insert the text "This is an output panel!" into it.
**Example with Error Messages**
```python
import sublime
import sublime_plugin
class CompileCodeCommand(sublime_plugin.WindowCommand):
def run(self):
panel = self.window.create_output_panel("compile_errors")
panel.run_command("insert", {"characters": "Compiling code...\n"})
try:
# Your code compilation logic here
pass
except Exception as e:
panel.run_command("insert", {"characters": str(e) + "\n"})
```
In this example, when you run the `CompileCodeCommand` command, it will create a new output panel named "compile_errors" in the active window and insert the text "Compiling code...\n" into it. If any exception occurs during the code compilation process, the error message will be appended to the output panel.
**Example with Syntax Highlighting**
```python
import sublime
import sublime_plugin
class RunScriptCommand(sublime_plugin.WindowCommand):
def run(self):
panel = self.window.create_output_panel("script_output")
panel.settings().set("syntax", "Packages/Python/Python.tmLanguage")
panel.run_command("insert", {"characters": "Running script...\n"})
try:
# Your script execution logic here
output = "Script output:\nHello, World!"
panel.run_command("insert", {"characters": output})
except Exception as e:
panel.run_command("insert", {"characters": str(e) + "\n"})
```
In this example, when you run the `RunScriptCommand` command, it will create a new output panel named "script_output" in the active window, set the syntax to Python, and insert the text "Running script...\n" into it. If the script execution is successful, it will append the script output to the panel with Python syntax highlighting. If any exception occurs, the error message will be appended to the output panel.
These are just a few examples of how you can use the `create_output_panel` function in Sublime Text 4 API. You can customize the output panel to suit your needs by using various methods and settings available in the API.

----
###### In Sublime Text 4 how can i Show Build Results, using my own target plugin?
(🦙 `From: LLama 3 • 70B`)

To show build results in Sublime Text 4 using your own target plugin, you can follow these steps:
1. **Create a `build_system` file**: In your plugin's directory, create a new file with a `.sublime-build` extension, for example, `my_build_system.sublime-build`.
2. **Define the build system**: In this file, define your build system using JSON. For example:
```json
{
"shell_cmd": "my_build_command",
"working_dir": "${project_path}",
"selector": "source.my_language"
}
```
Replace `my_build_command` with the actual command you want to run, `working_dir` with the directory where the command should be executed, and `selector` with the language scope of your plugin.
3. **Create a `Target` class**: In your plugin's Python code, create a new class that inherits from `sublime_plugin.Target`. For example:
```python
import sublime
import sublime_plugin
class MyBuildTarget(sublime_plugin.Target):
def run(self, edit, **kwargs):
# Run your build command here
print("Running my build command...")
#...
```
4. **Register the target**: In your plugin's `plugin.py` file, register the target using the `sublime_plugin.apply_target` decorator:
```python
@sublime_plugin.apply_target('my_build_target', 'y_build_system')
class MyBuildTarget(sublime_plugin.Target):
#...
```
Replace `my_build_target` with the name of your target class, and `my_build_system` with the name of your build system file (without the `.sublime-build` extension).
5. **Show build results**: To show the build results, you can use the `sublime.Window.show_quick_panel` method to display the output. For example:
```python
def run(self, edit, **kwargs):
# Run your build command here
output = subprocess.check_output(["my_build_command"])
window = sublime.active_window()
window.show_quick_panel([output.decode("utf-8")], lambda x: None, sublime.MONOSPACE_FONT)
```
This will display the build output in a quick panel.
That's it! With these steps, you should be able to show build results in Sublime Text 4 using your own target plugin.
If you need more help or have specific questions, feel free to ask!