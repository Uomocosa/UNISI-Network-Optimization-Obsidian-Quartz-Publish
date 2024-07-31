##### Original Sources:
- [Stack Overflow](https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python#:~:text=Because%20I%20routinely%20work%20with%20many%2Dgigabyte%20files%2C%20looping%20through%20as%20mentioned%20in%20the%20answers%20didn%27t%20work%20for%20me.%20The%20solution%20I%20use%3A)

---
##### Used in this file:
- 

---
###### ~ Ex.:
```python
def remove_last_line_from_file(file):
	file.seek(0, os.SEEK_END)
	pos = file.tell() - 1
	file.seek(pos, os.SEEK_SET)
	file.truncate()
	file.seek(0, 0)
	print(file.read())


with open(abs_path_to_file, "r+") as file:
	remove_last_line_from_file(file)
```

---
