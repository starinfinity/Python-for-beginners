import os
import sys
from os.path import exists

print("This is a file deletion script")
y = input("To Continue press Y Key \n").upper()
if not str(y) == "Y":
    sys.exit()
print("Is your file in current directory ?")
direct = input("Press Y for yes and N for no \n").upper()

if direct == "Y":
    print("Roger that!")
elif direct == "N":
    try:
        path = input("enter the path of file \n")
        os.chdir(path)
        print("Path set to %s" % path)
    except Exception as e:
        print("incorrect path or path does not exist")
        sys.exit()
else:
    print("invalid response")
    sys.exit()
print(os.listdir())
file_name = input("please enter the name of the file you want to delete \n")
if exists(file_name):
    print("Are you sure you want to permanently delete %s file" % file_name)
    confirmation = input("press Y for yes and any other key for no \n").upper()
    if confirmation == "Y":
        try:
            print("deleting the file %s" % file_name)
            os.remove(file_name)
        except Exception as e:
            print("file deletion error")
            sys.exit()
        print("file deletion successful")
        sys.exit()
    else:
        print("file not deleted")
        sys.exit()
else:
    print("file does not exist.")
    sys.exit()
