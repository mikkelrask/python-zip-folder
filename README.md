# Python Zip'n'Backup

A simple python script to frequently backup any folder, and automaticly upload it to Mega.nz. It is however made with a minecraft world folder in mind.

It utilizes [mega.py](https://pypi.org/project/mega.py/ "mega.py on PyPi.org") and the idea is to run it on a daily basis through a basic [cron job](https://en.wikipedia.org/wiki/Cron "Cron on Wiki"), or whatever equilant your OS offers.

The script will sorta check is the game is running, and will not execute if that is the case. This is to prevent chunk curruption i.e chunks that are being saved at the same time, as the script tries to backup or similar. Simply it will not run, if Java is running.

It should be able to run on every machine that has python installed, but have not been testet thuroughly.

![alt text](https://i.imgur.com/LnSj5FN.png "Screenshot of Zip'n'Backup in termite")

## Installing

**Download the script**

`git clone https://github.com/mikkelrask/python-zip-folder.git PATH-TO-YOUR-SAVES-FOLDER`

The path varies from OS to OS. Windows is typically
c:/Users/_Your Name_/AppData/Roaming/.minecraft/saves, while it's usually in ~/.minecraft/saves on unix like systems, like MacOS or most linux distros.

**Install requirements (mega.py)**

`pip install -r python-zip-folder/requirements.txt`
Will install mega.py and psutil. 

## Configuring

While mega uploads can be anonymized and do accept anonymous uploads, the script does assume you have a Mega.nz account and will not work if no account is given. Open up config.py in any text editor and put in your account credentials in (`user` and `password`), and put in the name if your world save folder name on (`folderName`), and hit save.

**One liners**
If you want to have more control or run multiple instances (to have more than one world backup, or back up to multiple accounts) you're also able to pass arguments through the commandline.

Ie:
`python App.py -u allan@yahoo.com -p ui1iIsmjz7/#,Ajkjc -w HawaiiMC -dl 1`

will download Allan's HawaiiMC backup from yesterday.

`-u` expects a string. This is your email for your Mega.nz account

`-p` expects a string. This is your password for your Mega.nz account

`-w` expects a string. With this one you are able to define what folder/world you want to backup.

`-dl` is of course optional and expects and integer representing how many backups/days you want to go back.
Note: If you put a blank space `` before your command including your password, this instance will not be saved in your shell history.

## Help

Run `python App.py --help`
