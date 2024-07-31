- ***Source***: [Youtube Playslist](https://www.youtube.com/watch?v=rly0g41UAzg&list=PLGfKZJVuHW91WyVIitRhcTPD1PTFIPsia)

---
- Inside of Sublime Text: `Tools >> Build System >> New Build System`

---
Official `python.sublime-build` file:
```json
{
	"cmd": ["python3", "-u", "$file"],
	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
	"selector": "source.python",
	
	"env": {"PYTHONIOENCODING": "utf-8"},
	
	"windows": {
		"cmd": ["py", "-u", "$file"],
	},

	"variants":
	[
		{
			"name": "Syntax Check",
			"cmd": ["python3", "-m", "py_compile", "$file"],
			
			"windows": {
				"cmd": ["py", "-m", "py_compile", "$file"],
			}
		}
	]
}
```
