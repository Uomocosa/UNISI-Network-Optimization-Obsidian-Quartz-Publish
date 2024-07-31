
```txt
Start the python virtual environment:
     1. cd to this folder.
     2. pipenv shell


Install the dependencies for this project:
     pipenv install

~Ex.: pipenv install numpy


REMEMBER to save the dependencies (updated the Lock file):
     pipenv lock

If you have changed the name of the folder, moved it or similar,
REMEBER to reinstall the venv, and the dependencies with:
     pipenv sync


----------- After the project is completed: -----------


Check vulnerabilities:
     pipenv check


Save the current versions of each package:
     pipenv lock

Install the pipfile.lock dependencies:
     pipenv install --ignore-pipfile
```

