import os
import zipfile
import datetime
from mega import Mega # install dependencies with 'pip install -r requirements.txt'

# IMPORTANT!
# Set your world name on line 46!

# Mega.NZ login
megaMail = '' # Insert your mail address for Mega.nz between the single quotes
megaPass = '' # Insert your password for Mega.nz between the single quotes
 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def retrieve_file_paths(dirName):
 
  filePaths = []
   
  for root, directories, files in os.walk(dirName):
    for filename in files:
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
         
  return filePaths

mega = Mega()

m = mega.login(megaMail, megaPass)



def main():
  world_name = 'worldname' # Insert the name of the folder you want to back up (your world name)
  now = str(datetime.datetime.today())
  ziparchive = world_name + now + '.zip'
  filePaths = retrieve_file_paths(world_name)

  print(bcolors.HEADER + '[+] Backing up world:' + bcolors.ENDC)
  for fileName in filePaths:
    print(fileName)

  print('')   
  print(bcolors.WARNING + '[!] This may take a while, depending on your world, computer specs and such.' + bcolors.ENDC)
  zip_file = zipfile.ZipFile(ziparchive, 'w')
  with zip_file:
    for file in filePaths:
      zip_file.write(file)
       
  print(bcolors.OKGREEN + '[+] ' + ziparchive + ' file was created successfully!' + bcolors.ENDC)
  print(bcolors.WARNING + '[!] Uploading .. Please wait.. ' + bcolors.ENDC)
  backup = m.upload(ziparchive)
  print(bcolors.OKGREEN + world_name + ' has been backed up to:' + bcolors.ENDC)
  link = m.get_upload_link(backup)
  print(bcolors.UNDERLINE + 'Mega link: ' + bcolors.BOLD + link + bcolors.ENDC)
  quota = m.get_storage_space(giga=True)
  print('')
  print('[i] You have now used '+ bcolors.OKGREEN + str(round(quota['used'], 2)) + ' GB' + bcolors.ENDC +  ' of your ' + bcolors.OKGREEN + str(quota['total']) + ' GB ' + bcolors.ENDC +'total on your Mega account.')
 


   
# Let's do this
if __name__ == "__main__":
  main()