from sys import *
import os

def DirectoryTravel(DirName):
    print("We are going to scan the directory :",DirName)

    for foldername,subfoldername,filename in os.walk(DirName):
        for fname in filename:
            print(fname)

    

def main():
    print("-----------Automation Script---------")

    print("Automation Script Name :",argv[0])

    if(len(argv)!=2):
        print("Invalid Number of Arguments")
        exit()

    if(argv[1]=='-h' or argv[1]=='-H'):
        print("This Automation script is used to perform file autoation")
        

    elif(argv[1]=='-u' or argv[1]=='-U'):
        print("Usage : Name of Script First_Argument")
        print("Example : Demo.py Marvellous(Folder Name)")
        exit()

    else:
        DirectoryTravel(argv[1])


if __name__ == "__main__":
    main()