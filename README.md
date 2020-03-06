# Python Zip'n'Backup

A simple python script i made to frequently backup my minecraft world, and automaticly upload it to Mega.nz. 

It utilizes [mega.py](https://pypi.org/project/mega.py/ "mega.py on PyPi.org")

![alt text](https://i.imgur.com/LnSj5FN.png "Screenshot of python-zip-folder in termite")

## Installing 
**Download the script**

```git clone https://github.com/mikkelrask/python-zip-folder.git```

**Copy the script to your saves folder**

```cp python-zip-folder/App.py PATH-TO-YOUR-SAVES-FOLDER```

The path varies from OS to OS. Windows is typically 

```c:/Users/*Your Name*/AppData/Roaming/.minecraft/saves```, while it's usually in 
```~/.minecraft/saves``` on unix like systems, like MacOS or most linux distros.


**Install requirements (mega.py)**


```pip install -r python-zip-folder/requirements.txt```


Now you can either run the script manually simply by typing:

```python App.py ```

while in your saves folder, or you can use a [cron job](https://en.wikipedia.org/wiki/Cron "Cron on Wiki") or similar, to do it for you, on a specific schedule.


## Configuring
While mega uploads can be anonymized, using the script assumes you have a Mega.nz account. Open up App.py in any text editor and put in your account credentials on line 10 and 11 (```megaMail``` and ```megaPass```), and put in the name if your world save folder name on line 46 (```world_name```), and hit save.
