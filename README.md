# context-menu-merge

Add ability to merge the selected folders in windows through the context menu

## Getting Started

These instructions will help you set up the program for you to use at your leisure

### Prerequisites

Python 3.6 is required for this project

In order to compile the script to an .exe for later execution
If you have pip in your path, then do the following:

```
pip install pyinstaller
```

If you don't, just add it to your PATH in system environment variables

### Setting up the menu

First compile the python file into an .exe, using the pyinstaller we installed

```
pyinstaller merge_folders.py
```

Locate the .exe that's created in the dist folder

Go to
```
C:\Users\<your user>\AppData\Roaming\Microsoft\Windows\SendTo
```
make a shortcut that targets the .exe of the python script you've created

If you've done everything properly, it should look like this

![Alt text](./context_menu.png?raw=true "like this")
Note* I customized the icon, you can do the same under properties of the shortcut after you created it 

And now you can right click any amount of folders and put the content of each into a merged folder