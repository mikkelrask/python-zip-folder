import os
import zipfile
import datetime
from mega import Mega # install dependencies with pip install -r requirements.txt
import argparse

# Mega.NZ login
megaMail = '' # Insert your mail address for Mega.nz between the single quotes
megaPass = '' # Insert your password for Mega.nz between the single quotesquotes

worldFolder = '' # Type the name of the directory/world you want to backup

# Nothin below here really needs to be edited

parser = argparse.ArgumentParser("python App.py")
parser.add_argument("-u", "--user", type=str, help="Mega.NZ username (overrules megaMail set in script")
parser.add_argument("-p", "--passw", type=str, help="Mega.NZ password (overrules megaPass set in script")
parser.add_argument('-w', '--world', type=str, help="Name of the folder/world to back up (overrules worldFolder set in script")
args = parser.parse_args()

passed_user = args.user
passed_password = args.passw
passed_worldname = args.world


class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FAIL = '\033[91m'

def retrieve_file_paths(dirName):
 
  filePaths = []
   
  for root, directories, files in os.walk(dirName):
    for filename in files:
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
         
  return filePaths

mega = Mega()

if passed_user != None:
  if passed_password == None:
    passed_password = input('Type the Mega.nz password for user ' + passed_user + ': ')
  m = mega.login(passed_user, passed_password)
elif megaMail and megaPass != '':
  m = mega.login(megaMail, megaPass)
else:
  print(bcolors.FAIL + 'No account settings found for Mega.nz' + bcolors.ENDC)
  print('Run with --help for more info')
  exit()


def main():
  if str(args.world) != 'None':
    world = str(args.world)
  else:
    world = worldFolder

  if world == '':
    print(bcolors.FAIL + 'No world folder set.' + bcolors.ENDC)
    print('Run --help for more info')
    exit()


  now = str(datetime.datetime.today().date())
  ziparchive = world + '.' + now + '.zip'
  filePaths = retrieve_file_paths(world)

  print(bcolors.HEADER + '[+]'+ bcolors.ENDC +' Backing up '+world+':')
  for fileName in filePaths:
    print(fileName)

  print('')   
  print(bcolors.WARNING + '[!] This may take a while, depending on your world, computer specs and such.' + bcolors.ENDC)
  zip_file = zipfile.ZipFile(ziparchive, 'w')
  with zip_file:
    for file in filePaths:
      zip_file.write(file)
       
  print(bcolors.OKGREEN + '[+] ' + bcolors.ENDC + ziparchive + ' file was created successfully!')
  folder = m.find('mcbackup')
  print(bcolors.WARNING + '[!]' + bcolors.ENDC +' Uploading .. Please wait.. ')
  backup = m.upload(ziparchive, folder)
  print(bcolors.OKGREEN + world  + bcolors.ENDC+ ' has been backed up to following Mega link:')
  link = m.get_upload_link(backup)
  print(bcolors.UNDERLINE + bcolors.BOLD + link + bcolors.ENDC)
  quota = m.get_storage_space(giga=True)
  print('')
  print('[i] You have now used '+ bcolors.OKGREEN + str(round(quota['used'], 2)) + ' GB' + bcolors.ENDC +  ' of your ' + bcolors.OKGREEN + str(quota['total']) + ' GB ' + bcolors.ENDC +'total on your Mega account.')
 


   
# Let's do this
if __name__ == "__main__":
  main()
