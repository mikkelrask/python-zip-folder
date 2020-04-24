import os
import zipfile
import datetime
from mega import Mega
import argparse

# Mega.NZ login
megaMail = ''  # email for Mega.nz account
megaPass = ''  # password for Mega.nz account

worldFolder = ''  # Folder to backup


# Nothin below here really needs to be edited
class bcolors:  # Set the colors we use
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FAIL = '\033[91m'


parser = argparse.ArgumentParser('python App.py')  # The --help section
parser.add_argument('-u', '--user', type=str,
                    help='Your Mega.NZ username. Usage: '
                    + bcolors.OKGREEN + ' python App.py -u \
                    youremail@megaaccount.nz'
                    + bcolors.ENDC + ' (overrules megaMail set in script)')
parser.add_argument('-p', '--password', type=str, help='Mega.NZ password\
                    (overrules megaPass set in App.py)')
parser.add_argument('-w', '--world', type=str,
                    help='Name of the folder/world\
                    to back up (overrules worldFolder set in App.py')
parser.add_argument('-dl', '--download', type=int,
                    help='Download and unpack\
                    backups. Usage: ' + bcolors.OKGREEN + ' python App.py\
                    -dl 1 ' + bcolors.ENDC + 'where 1 indicates how many\
                    days/backups you want to go.')
args = parser.parse_args()

passed_user = args.user
passed_password = args.password
passed_worldname = args.world
dl = args.download

mega = Mega()  # Initiate Mega lib


# Check if user and pass is set or passed
if passed_user is not None:
  if passed_password is None:
    passed_password = input('Type the Mega.nz password for user '
                            + passed_user + ': ')
  m = mega.login(passed_user, passed_password)
elif megaMail and megaPass is not '':
  m = mega.login(megaMail, megaPass)
else:
  print(bcolors.FAIL + 'No account settings found for Mega.nz'
        + bcolors.ENDC)
  print('Run ' + bcolors.OKGREEN + 'python App.py --help'
        + bcolors.ENDC + ' for more info')
  exit()


if str(args.world) is not 'None':
  world = str(args.world)
else:
  world = worldFolder


if world == '':
  print(bcolors.FAIL + 'No world folder set.' + bcolors.ENDC)
  print('Run ' + bcolors.OKGREEN + 'python App.py --help'
        + bcolors.ENDC + ' for more info')
  exit()


# The download backup functionality
def download_backup():
  days_back = dl - 1
  linklist = []
  filenamelist = []
  files = m.get_files()

  for node in files:  # cycle through what we are getting back from Mega
      newnode = files.get(node)
      name = newnode['a']
      filename = name['n']
      if world in filename:
          link = m.export(filename)
          filenamelist.append(filename)
          linklist.append(link)

  location = os.getcwd()
  print(bcolors.WARNING + '[!]' + bcolors.ENDC + ' Mining duped world from '
        + bcolors.WARNING + str(dl) + bcolors.ENDC + ' days ago.. Please wait')
  filenamelist.sort(reverse=True)
  linklist.sort(reverse=True)
  dllink = (str(linklist[days_back]))
  dlfile = str(filenamelist[days_back])
  m.download_url(dllink, location)
  print(bcolors.OKGREEN + '[+]' + bcolors.ENDC + ' Mining complete')
  print(bcolors.WARNING + '[!]' + bcolors.ENDC + ' Crafting world from dupe - \
        this will just take a tick, almost there')
  with zipfile.ZipFile(dlfile, 'r') as zipObj:
    # Extract all the contents of zip file in current directory
    zipObj.extractall()
  print(bcolors.OKGREEN + 'Success! Grab your pickaxe and go mine!'
        + bcolors.ENDC)


if args.download is not None:
  download_backup()
  exit()


def retrieve_file_paths(dirName):  # figure out what we are backing up
  filePaths = []

  for root, directories, files in os.walk(dirName):
    for filename in files:
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)

  return filePaths


def main():
  now = str(datetime.datetime.today().date())
  ziparchive = world + now + '.zip'
  filePaths = retrieve_file_paths(world)

  print(bcolors.HEADER + '[+]' + bcolors.ENDC + ' Duping ' + world + ':')
  for fileName in filePaths:
    print(fileName)

  print('')
  print(bcolors.WARNING + '[!] Crafting a shulker box with your world \
        inside. This may have the Slowness effect depending on your \
        world size, computers specs and such.' + bcolors.ENDC)
  zip_file = zipfile.ZipFile(ziparchive, 'w')
  with zip_file:
    for file in filePaths:
      zip_file.write(file)

  print(bcolors.OKGREEN + '[+] ' + bcolors.ENDC + ziparchive
        + ' shulker was crafted successfully!')
  folder = m.find('mcbackup')
  print(bcolors.WARNING + '[!]' + bcolors.ENDC + ' Uploading .. \
        Please wait.. ')
  backup = m.upload(ziparchive, folder)
  print(bcolors.OKGREEN + world + bcolors.ENDC + ' has been duped \
        like TNT and sent to your sorting system:')
  link = m.get_upload_link(backup)
  print(bcolors.UNDERLINE + bcolors.BOLD + link + bcolors.ENDC)
  quota = m.get_storage_space(giga=True)
  print('')
  print(bcolors.WARNING + '[!]' + bcolors.ENDC + 'Tidying up - \
        throwing local shulker in lava')
  os.remove(backup)
  print('[i] You have now used ' + bcolors.OKGREEN
        + str(round(quota['used'], 2)) + ' GB' + bcolors.ENDC
        + ' of your ' + bcolors.OKGREEN + str(quota['total'])
        + ' GB ' + bcolors.ENDC + 'total in your \
        sorting systems inventory.')


# Let's do this
if __name__ == '__main__':
  main()
