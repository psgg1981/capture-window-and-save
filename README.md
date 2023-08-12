# capture-window-and-save
Windows automation of MSPaint for quick saving of screenshots

## Requirements

### Python 
Windows: 
- install Python from https://www.python.org/downloads/
- install pip (see https://pip.pypa.io/en/stable/installation/)

Run the following command to install the dependencies

`pip install pywinauto`

## Configuration

### Making it accessible from Windows Path

1. Copy your pywinauto directory path

2. Go to Windows Start menu > type "env" and open "Edit the system environment variables"

3. Click "Environment Variables..."

4. Select 'Path', then click Edit

5. Click New and paste the value from #1

### Creating an executable for simpler usage

Install pyinstaller via pip

`pip install pyinstaller`

Compile python file into 1 executable

`pyinstaller --onefile capture-window-and-save.py`

Copy the executable file onto the existing directory (already reacheable from Windows Path)

`copy dist\capture-window-and-save.exe .`

### Execution 

Just call 

`capture-window-and-save`

or 

`capture-window-and-save.exe`

from anywhere (if you set it up from Windows Path). Snapshots will be stored in the original directory
