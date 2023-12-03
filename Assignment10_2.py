from sys import *
import os
import time

def DirectoryTravel(DirName,extension1,extension2):
    print("We are going to Scan the Directory : ",DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                if fname.endswith(extension1):
                    old_file_path = os.path.join(foldername, fname)
                    new_file_path = os.path.join(foldername, os.path.splitext(fname)[0] + extension2)

                    # Rename the file
                    os.rename(old_file_path, new_file_path)
                    
        print("Extension Changed Successfully")
                    
    else:
        print("Invalid path")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument Second_Argument")
        print("Example : Directory Rename.py satyam .doc .txt")
        exit()

    if(len(argv) != 4):
        print("Invalid number of arguments")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1],argv[2],argv[3])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name File_Name