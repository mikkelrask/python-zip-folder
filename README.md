# Python Zip'n'Backup

A simple python script i made to frequently backup my minecraft world, and automaticly upload it to Mega.nz. 

It utilizes [mega.py](https://pypi.org/project/mega.py/ "mega.py on PyPi.org") and the idea is to run it on a daily basis through a basic [cron job](https://en.wikipedia.org/wiki/Cron "Cron on Wiki"), or whatever equilant your OS offers.

It should be able to run on every machine that has python installed, but have not been testet 

![alt text](https://i.imgur.com/LnSj5FN.png "Screenshot of Zip'n'Backup in termite")

## Installing 
**Download the script**

```git clone https://github.com/mikkelrask/python-zip-folder.git```

**Copy the script to your saves folder**

```cp python-zip-folder/App.py PATH-TO-YOUR-SAVES-FOLDER```

The path varies from OS to OS. Windows is typically 
c:/Users/*Your Name*/AppData/Roaming/.minecraft/saves, while it's usually in ~/.minecraft/saves on unix like systems, like MacOS or most linux distros.


**Install requirements (mega.py)**


```pip install -r python-zip-folder/requirements.txt```


Now you can either run the script manually simply by typing:

```python App.py ```

while in your saves folder, or you can use a cron job or similar, to do it for you, on a specific schedule.


## Configuring
While mega uploads can be anonymized, using the script assumes you have a Mega.nz account. Open up App.py in any text editor and put in your account credentials in (```megaMail``` and ```megaPass```), and put in the name if your world save folder name on (```world_name```), and hit save.

## One liners
If you want to have more control or run multiple instances (to have more than one world backup, or back up to multiple accounts) you're also able to pass arguments through the commandline.

Ie:
```python App.py -u allan@yahoo.com -p ui1iIsmjz7/#,Ajkjc -w HawaiiMC -dl 1```

will download Allan's HawaiiMC backup from yesterday.

```-u``` expects a string. This is your email for your Mega.nz account

```-p``` expects a string. This is your password for your Mega.nz account

```-w``` expects a string. With this one you are able to define what folder/world you wan't to backup.

```-dl``` is of course optional and expects and integer representing how many backups/days you want to go back.

## Help
Run ```python App.py --help```
