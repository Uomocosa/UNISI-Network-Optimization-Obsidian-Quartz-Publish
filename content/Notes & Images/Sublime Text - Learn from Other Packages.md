
One of the best way to learn how packages work, is to see the source code behind each plugin.
> [Finding Commands by "OdatNurd"](https://www.youtube.com/watch?v=XXaxkhFg83U)
>  - To see which command is being executed open the [[Sublime Text - Sublime Console|console]] and write `sublime.log_commands(True)`

^9175d4

Generally to see the inside of a plugin you can follow this list:
- Do to that open the [[Sublime Text - Command Palette|comand palette]] and digit "**vpf**" or "View Package FIle"
- Then digiti "**py**" or "**.py**" (to search between all the file with the python extension - these files are all [[Sublime Text - Sublime Plugins|plugins]] - )
- Then select one of them to see the source code.
> Also once you have open a plugin, you can see its location on the top of the IDE, it should be somenthing like:
> "C:\Program Files (x86)\Sublime Text\Data\ Packages\ Default\fold.py - Sublime Test (UNREGISTRED)"