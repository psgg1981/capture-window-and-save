import os, logging
from pywinauto.application import Application
from pywinauto import keyboard
from datetime import datetime

logging.basicConfig(level=logging.INFO)     # logger

keyboard.send_keys('%{TAB}')                # ALT+Tab (switch to immediate window behind)
keyboard.send_keys('%{PRTSC}')              # print screen
#keyboard.send_keys('%{TAB}')               # ALT+Tab (get back to )
app = Application().start(cmd_line=u'"C:\\Windows\\System32\\mspaint.exe" ')
mspaintapp = app.MSPaintApp
mspaintapp.wait('ready')
keyboard.send_keys('^V')                    # paste
keyboard.send_keys('^S')                    # save
dir = os.getcwd().replace(' ', '{SPACE}')   # replace whitespace with {SPACE} key
logging.debug(dir)                         # debug directory print
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = timestamp+".png"
keyboard.send_keys(dir+'\\'+filename, pause=0)    # save file
keyboard.send_keys('{ENTER}')
keyboard.send_keys('%{F4}')                 # exit program
#keyboard.send_keys('%{TAB}')                # get back to previous window
print(filename + ' saved.') 