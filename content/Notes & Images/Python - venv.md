> ***Alternative***: Use [[Docker - Container for Python]] (it sucks)

##### On **CLI**:
1. Move to the desired location using `cd`.<br>**REMEBER**: if you want to go to another directory (C:\\ ⇒ D:\\) use `cd \d`.
2. `python -m venv [VIRUTAL ENVIRONMENT NAME]`<br>**NOTE**: This will create a new folder.
3. `cd [VIRUTAL ENVIRONMENT NAME]``
4. `Scripts\activate.bat`
5. To install modules and packages **only on the virtual environment** use
   `python -m pip install [PACKAGE NAME]`
5. To exit the virtual environment:
   `Scripts\deactivate.bat`

---
##### On **CLI** - Similar Way:
1. Move to the desired location using `cd`.<br>**REMEBER**: if you want to go to another directory (C:\\ ⇒ D:\\) use `cd \d`.
2. `python -m venv [VIRUTAL ENVIRONMENT NAME]`<br>**NOTE**: This will create a new folder.
3. `[VIRUTAL ENVIRONMENT NAME]\Scripts\activate.bat`
4. To install modules and packages **only on the virtual environment** use
   `python -m pip install [PACKAGE NAME]`
5. To exit the virtual environment:
   `[VIRUTAL ENVIRONMENT NAME]\Scripts\deactivate.bat

---
##### Move/Sync your Virtual Environment (Method I):
*(TO BE TESTED, not sure if it will work)*
1. Create **2** virtual environments (where you want to move/sync)
2. After installing the wanted libraries use the command
   `python -m pip freeze > requirements.txt`I
3. In the other virtual environment use the command:
   `python -m pip install -r requirements.txt`
- **Source**: [StackOverflow](https://stackoverflow.com/questions/9207430/how-to-copy-clone-a-virtual-environment-from-server-to-local-machine)

---
##### Move/Sync your Virtual Environment (Method II):
1. Create **2** virtual environments (where you want to move/sync)
2. Copy everything exepts the `Scripts` folder from venv_1 to venv_2
3. *(Optional)*: With Syncthing we can add to the ingore patterns *Scripts*, this will exclude the `Scripts` folder to be synced

---
##### On **Sublime Text**:
1. Create a new project in the : `[VIRUTAL ENVIRONMENT NAME]` directory just created.
   `Hamburger Menu -> Project -> Save Project As`
2. Once it has create a project it will also create a `.sublime-project` file and a `.sublime-workspace` file, in the `.sublime-project` file past this code (changed accordingly)
   ```json
   {
	"folders":
	[
		{
			"path": ".."
		}
	],
	"build_systems":
	[
		{
			"name" : "[BUILD SYSTEM NAME]",
			"cmd": ["$folder/Scripts/python.exe", "$file"],
			"selector": "source.python",
			"file_regex": "^\\s*File \"(...*?)\", line ([0-9]*)"
		}
	]
}
   ```

---
# Online Resources
- [Online ‘venv’ explenation](https://www.youtube.com/watch?v=APOPm01BVrk) 
- [Python Official Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Sublime Text Official Documentation](https://www.sublimetext.com/docs/build_systems.html)
