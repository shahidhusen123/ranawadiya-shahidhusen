# # # Project Name : Auto File Organization
# # # Name : SHAHIDHUSEN RANAWADIYA
# # # Enrollment No. :21SOECE13042
# # # Class : 3CED


import os
import shutil

# reading the folder's file
folderpath = r"Folder Path which are copy from this file."
os.chdir(folderpath)
os.getcwd()

# # check the files
os.listdir()

# #get extension
list_extension = []
for fl in os.listdir():
    extension = fl.split(".")[-1]
    list_extension.append(extension)
    # print(list_extension)

list_extension = set(list_extension)
print(list_extension)
print(len(list_extension))

# # create a folder on the desktop
path = os.environ["UserProfile"] + "\\" + "Desktop" + "\\" + "Folder Name(Create a folder name)"
print(path)
os.mkdir(path)
try:
    shutil.rmtree(path)
    os.mkdir(path)
except:
    os.mkdir(path)

# # we can transfer the file with specific folder
for ex in list_extension:
    print(ex, end=",")
    os.mkdir(path + "\\" + ex)
    for fl in os.listdir():
        if ex in fl:
            shutil.copy(fl, path + "\\" + ex)