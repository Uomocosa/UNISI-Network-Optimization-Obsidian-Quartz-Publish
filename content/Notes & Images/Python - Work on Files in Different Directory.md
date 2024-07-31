# Work on Files in Different Directory

```python
current_dir = os.getcwd()
relative_path = "child_1/child_2"
file_name = "porva_1"

absolute_path_to_file = os.path.join(
	current_dir,
	relative_path,
	file_name,
)

letter_for = {
	read : 'r',  #open for reading (default)
	write: 'w',  #open for writing, truncating the file first
	create: 'x', #open for exclusive creation, 
				 #failing if the file already exists
	append: 'a', #open for writing, appending to the 
				 #end of file if it exists
	binary: 'b', #binary mode
	text: 't',   #text mode (default)
}

with open(absolute_path_to_file, letter_for[read]) as file:
	string = file.read('')

```