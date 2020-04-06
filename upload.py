from mega import Mega

mega = Mega()
m = mega.login("mikkelrask@pm.me", "mmne4mMicf4LsMk")
folder = m.find('mcbackup', exclude_deleted=True)
m.upload('worldname2020-03-07 23:51:34.350327.zip', folder[0])

files = m.get_files()
print(files)