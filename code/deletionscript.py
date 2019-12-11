#Author Rahul Gahlot
#github.com/starinfinity

#simple python script to delete file
import os
import sys
from os.path import exists

x = 1
print("This is a file deletion script")
y = input("To Continue press Y Key \n").upper()
#check whether input is yes or not

if not str(y) == "Y":
    print("Thank you for using this script")
    sys.exit()
#while loop to delete multiple files
while x == 1:
    f = 1
    print("Is your file in current directory ?")
    direct = input("Press Y for yes and N for no \n").upper()
#while loop for multiple attempts in providing path
    while f == 1:

        if direct == "Y":
            print("Roger that!")

        elif direct == "N":
#change path as per input by user
            try:
                path = input("enter the path of file \n")
                os.chdir(path)
                print("Path set to %s" % path)
                f = 0
#handle the exception is path is incorrect
            except Exception as e:
                print("Incorrect path or path does not exist")
                print("Do you wish to continue?")
                perm = input("Press Y for yes and any other key for NO").upper()
                if perm != "Y":
                    print("Thank you for using this script")
                    sys.exit()
                else:
                    print("press .(dot) for same directory")

        else:
            print("invalid response")
            print("Do you want to continue?")
            cont = input("press Y for YES. Any other key for NO.").upper()

            if cont != "Y":
                print("Thank You for using this script")
                sys.exit()
#list all files in current directory
    print(os.listdir())
    file_name = input("please enter the name of the file you want to delete \n")
#check whether file exists or not. if yes delete it.
    if exists(file_name):
        print("Are you sure you want to permanently delete %s file" % file_name)
        confirmation = input("press Y for yes and any other key for no \n").upper()

        if confirmation == "Y":

            try:
                print("deleting the file %s" % file_name)
                os.remove(file_name)
                print("file deletion successful")

            except Exception as e:
                print("file deletion error")
                sys.exit()

        else:
            print("file not deleted")
            sys.exit()

    else:
        print("file does not exist.")

    print("Do you want to delete another file ? ")
    another = input("press Y for YES or any other key for NO \n").upper()

    if another != "Y":
        print("Thank you for using this script")
        sys.exit()

    else:
        print("continue deleting another file")
