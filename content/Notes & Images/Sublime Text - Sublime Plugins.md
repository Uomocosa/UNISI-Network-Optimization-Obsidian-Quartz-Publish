
Sublime Plugins are just python files in a folder (named as you deemed appropiate) in the [[Sublime Text - Package Folder|Package folder]].
A plugin can changed almost everything Sublime Text does, and/or add new functionality.
> **NOTE THAT:** a plugin is written in a **pre-installed version of python** found in the sublime text folder, this version cannot be upgraded/downgraded by the user.
> If you want to know which version of python Sublime Text is using when creating a plugin you can type 
`import sys `
`sys.version`
> In the [[Sublime Text - Sublime Console|console]]