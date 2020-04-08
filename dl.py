import os
import zipfile
import datetime
from mega import Mega # install dependencies with pip install -r requirements.txt

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FAIL = '\033[91m'

email = ""
password = ""
world = "HawaiiNEW"

mega = Mega()
m = mega.login("", "")
files = m.get_files()
for node in files:
    newnode = files.get(node)
    name = newnode['a']
    filename = name['n']
    linklist = []
    filenamelist = []
    if world in filename:
        link = m.export(filename)
        location = os.getcwd()
        print('Downloading latest backup.. Please wait')
        m.download_url(link, location)