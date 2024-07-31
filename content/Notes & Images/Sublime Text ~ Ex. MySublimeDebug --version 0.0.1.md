> **NOTE**:
>  **IT SUCKS**, because it negates all the other plugins, it is higly recommended to never use this code again, its not bad written, it is **all** the implementation wrong, still here it is to know **what NOT TO DO**:

In 'Programs Files (x86)\\Sublime Text\\Data\\Packages\\MySublimeDebug' (a new Folder I created)
```python
import sublime
import sublime_plugin

buffer = ""

# THIS ONLY WORKS WITH THE 
# 'Default.sublime-keymaps' IN THE 'User' FOLDER

# OR MAYBE NOT, 
#	NEED TO CHECK IF KEEPIN THE 'Default.sublime-keymaps'
# 	in this Folder those the jobs 


def fill_buffer_searching_for(
	buffer: str, 
	key_pressed: str, 
	text_to_search: str
) -> str:
	if not text_to_search: return buffer + key_pressed

	print("len(buffer) = " + str(len(buffer)))
	
	buffer += key_pressed

	return buffer


def what_to_do_on_key_pressed(key_pressed):
	print("key_pressed = " + str(key_pressed))
	#DONT know why, but f"" doesnt work
	global buffer
	buffer = fill_buffer_searching_for(buffer, key_pressed, "\nD(")

	print("buffer = " + buffer)


# NOTE: This function work in combo with the Default.sublime-keymap 
# locatedin the User folder, IT'S NOT COMPLETED, it misses some chars
class ExecuteFunctionWhenKeyIsPressedCommand(sublime_plugin.TextCommand):
	def run(self, edit, **kargs):
		key_pressed = kargs["keystroke"]
		

		what_to_do_on_key_pressed(key_pressed)


		RC = self.view.run_command
		
		if key_pressed == "BACKSPACE":
			RC("left_delete")

		elif key_pressed == "DELETE":
			RC("right_delete")

		elif key_pressed == "ENTER":
			RC( "commit_completion")
			RC("insert", {"characters": "\n"})
			
		elif key_pressed == "TAB":
			RC("insert", {"characters": "\t"})
			

		else:
			RC("insert", {"characters": key_pressed})
```


In 'Programs Files (x86)\\Sublime Text\\Data\\Packages\\User' (always found in the 'Package' Folder)
```python
[
    { "keys": ["a"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "a" } },
    { "keys": ["b"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "b" } },
    { "keys": ["c"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "c" } },
    { "keys": ["d"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "d" } },
    { "keys": ["e"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "e" } },
    { "keys": ["f"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "f" } },
    { "keys": ["g"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "g" } },
    { "keys": ["h"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "h" } },
    { "keys": ["i"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "i" } },
    { "keys": ["j"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "j" } },
    { "keys": ["k"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "k" } },
    { "keys": ["l"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "l" } },
    { "keys": ["m"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "m" } },
    { "keys": ["n"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "n" } },
    { "keys": ["o"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "o" } },
    { "keys": ["p"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "p" } },
    { "keys": ["q"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "q" } },
    { "keys": ["r"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "r" } },
    { "keys": ["s"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "s" } },
    { "keys": ["t"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "t" } },
    { "keys": ["u"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "u" } },
    { "keys": ["v"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "v" } },
    { "keys": ["w"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "w" } },
    { "keys": ["x"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "x" } },
    { "keys": ["y"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "y" } },
    { "keys": ["z"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "z" } },


    { "keys": ["A"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "A" } },
    { "keys": ["B"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "B" } },
    { "keys": ["C"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "C" } },
    { "keys": ["D"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "D" } },
    { "keys": ["E"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "E" } },
    { "keys": ["F"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "F" } },
    { "keys": ["G"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "G" } },
    { "keys": ["H"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "H" } },
    { "keys": ["I"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "I" } },
    { "keys": ["J"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "J" } },
    { "keys": ["K"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "K" } },
    { "keys": ["L"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "L" } },
    { "keys": ["M"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "M" } },
    { "keys": ["N"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "N" } },
    { "keys": ["O"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "O" } },
    { "keys": ["P"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "P" } },
    { "keys": ["Q"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "Q" } },
    { "keys": ["R"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "R" } },
    { "keys": ["S"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "S" } },
    { "keys": ["T"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "T" } },
    { "keys": ["U"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "U" } },
    { "keys": ["V"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "V" } },
    { "keys": ["W"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "W" } },
    { "keys": ["X"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "X" } },
    { "keys": ["Y"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "Y" } },
    { "keys": ["Z"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "Z" } },

    { "keys": ["0"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "0" } },
    { "keys": ["1"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "1" } },
    { "keys": ["2"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "2" } },
    { "keys": ["3"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "3" } },
    { "keys": ["4"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "4" } },
    { "keys": ["5"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "5" } },
    { "keys": ["6"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "6" } },
    { "keys": ["7"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "7" } },
    { "keys": ["8"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "8" } },
    { "keys": ["9"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "9" } },

    { "keys": [" "], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": " " } },

    { "keys": ["\\"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "\\" } },
    { "keys": ["|"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "|" } },
    { "keys": ["!"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "!" } },
    { "keys": ["\""], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "\"" } },
    { "keys": ["£"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "£" } },
    { "keys": ["$"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "$" } },
    { "keys": ["%"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "%" } },
    { "keys": ["&"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "&" } },
    { "keys": ["/"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "/" } },
    { "keys": ["("], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "(" } },
    { "keys": [")"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": ")" } },
    { "keys": ["="], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "=" } },
    { "keys": ["'"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "'" } },
    { "keys": ["?"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "?" } },
    { "keys": ["ì"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "ì" } },
    { "keys": ["^"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "^" } },
    { "keys": ["-"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "-" } },
    { "keys": ["_"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "_" } },
    { "keys": ["."], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "." } },
    { "keys": [":"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": ":" } },
    { "keys": [","], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "," } },
    { "keys": [";"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": ";" } },
    { "keys": ["<"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "<" } },
    { "keys": [">"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": ">" } },
    { "keys": ["è"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "è" } },
    { "keys": ["é"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "é" } },
    { "keys": ["["], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "[" } },
    { "keys": ["{"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "{" } },
    { "keys": ["+"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "+" } },
    { "keys": ["*"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "*" } },
    { "keys": ["]"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "]" } },
    { "keys": ["}"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "}" } },
    { "keys": ["ò"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "ò" } },
    { "keys": ["ç"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "ç" } },
    { "keys": ["@"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "@" } },
    { "keys": ["à"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "à" } },
    { "keys": ["°"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "°" } },
    { "keys": ["#"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "#" } },
    { "keys": ["ù"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "ù" } },
    { "keys": ["§"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "§" } },
    

    //{ "keys": ["enter"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "ENTER" } },



    { "keys": ["backspace"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "BACKSPACE" }, },
    { "keys": ["enter"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "ENTER" }, },
    { "keys": ["tab"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "TAB" }, },
    { "keys": ["delete"], "command": "execute_function_when_key_is_pressed", "args": {"keystroke": "DELETE" }, },
    
]
```