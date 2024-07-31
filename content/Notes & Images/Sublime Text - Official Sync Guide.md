- ***Source***: [Sublime Text Official](https://packagecontrol.io/docs/syncing#dropbox-linux)
---
# Syncing

To properly sync your installed packages across different machines, you actually do **not** want to sync the whole Packages/ and Installed Packages/ folders. The reason for this is that some packages have different versions for different operating systems. By syncing the actual package contents across operating systems, you will possibly run into broken packages.

The proper solution is to install Package Control on all machines and then to sync only the Packages/User/ folder. This folder contains the Package Control.sublime-settings file, which includes a list of all installed packages. If this file is copied to another machine, the next time Sublime Text is started, Package Control will install the correct version of any missing packages.

## Using Git

Many developers are familiar with Git, and it is a logical choice for keeping files in sync across machines if you don't mind a little manual work. There are a few things to keep in consideration when using Git:
- If you use a service like GitHub and do not use a private repository, you may accidentally share license keys for any commercial packages you have purchased.
- Certain files and folders in the Packages/User/ folder change regularly, so you may want to add them to a .gitignore file. There is really no harm in syncing these, however some of them change on an hourly basis, which may result in having to run more Git commands. Examples include:
	- Package Control.last-run
    - Package Control.ca-list
    - Package Control.ca-bundle
    - Package Control.system-ca-bundle
    - Package Control.cache/
    - Package Control.ca-certs/

## Using Dropbox

Dropbox is another popular choice for syncing settings. It has the benefit of automatically syncing files and not having to worry about privacy. In order to use this properly, symlinks must be set up via the command line. The following instructions should provide some guidance.

- [Windows instructions](https://packagecontrol.io/docs/syncing#dropbox-windows)
- [Mac instructions](https://packagecontrol.io/docs/syncing#dropbox-osx)
- [Linux instructions](https://packagecontrol.io/docs/syncing#dropbox-linux)

### Windows

These instructions work for Windows Vista and newer, but unfortunately do not work for Windows XP. If your Dropbox folder is not in the default location, you'll need to change `$env:userprofile\Dropbox` to your location.

1. Close Sublime Text
2. Open PowerShell by right-clicking and selecting _Run as administrator_

#### First Machine

On your first machine, use the following instructions.

[Sublime Text 3](https://packagecontrol.io/docs/syncing#)[Sublime Text 2](https://packagecontrol.io/docs/syncing#st2)

cd "$env:appdata\Sublime Text 3\Packages\"
mkdir $env:userprofile\Dropbox\Sublime
mv User $env:userprofile\Dropbox\Sublime\
cmd /c mklink /D User $env:userprofile\Dropbox\Sublime\User

#### Other Machine(s)

On your other machine(s), use the following instructions. **These instructions will remove your _User/_ folder and all contents!**

[Sublime Text 3](https://packagecontrol.io/docs/syncing#)[Sublime Text 2](https://packagecontrol.io/docs/syncing#st2)

cd "$env:appdata\Sublime Text 3\Packages\"
rmdir -recurse User
cmd /c mklink /D User $env:userprofile\Dropbox\Sublime\User

### Mac

If your Dropbox folder is not in the default location, you'll need to change `~/Dropbox` to your location.

1. Close Sublime Text
2. Open Terminal

#### First Machine

On your first machine, use the following instructions.

[Sublime Text 3](https://packagecontrol.io/docs/syncing#)[Sublime Text 2](https://packagecontrol.io/docs/syncing#st2)

cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
mkdir ~/Dropbox/Sublime
mv User ~/Dropbox/Sublime/
ln -s ~/Dropbox/Sublime/User

#### Other Machine(s)

On your other machine(s), use the following instructions. **These instructions will remove your _User/_ folder and all contents!**

[Sublime Text 3](https://packagecontrol.io/docs/syncing#)[Sublime Text 2](https://packagecontrol.io/docs/syncing#st2)

cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
rm -r User
ln -s ~/Dropbox/Sublime/User

### Linux

If your Dropbox folder is not in the default location, you'll need to change `~/Dropbox` to your location.

1. Close Sublime Text
2. Open Terminal

#### First Machine

On your first machine, use the following instructions.

[Sublime Text 3](https://packagecontrol.io/docs/syncing#)[Sublime Text 2](https://packagecontrol.io/docs/syncing#st2)

cd ~/.config/sublime-text-3/Packages/
mkdir ~/Dropbox/Sublime
mv User ~/Dropbox/Sublime/
ln -s ~/Dropbox/Sublime/User

#### Other Machine(s)

On your other machine(s), use the following instructions. **These instructions will remove your _User/_ folder and all contents!**

[Sublime Text 3](https://packagecontrol.io/docs/syncing#)[Sublime Text 2](https://packagecontrol.io/docs/syncing#st2)

cd ~/.config/sublime-text-3/Packages/
rm -r User
ln -s ~/Dropbox/Sublime/User
