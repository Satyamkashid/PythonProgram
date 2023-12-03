from sys import *
import os

def DirectoryTravel(DirName):
    print("We are going to scan the directory :",DirName)

    for foldername,subfoldername,filename in os.walk(DirName):
        print("Current directory name :",foldername)

        for subname in subfoldername:
            print("Subfolder name is",subname)

        for fname in filename:
            print(fname)

def main():
    print("-------Automation Script------")

    print("Automation script name :",argv[0])

    if(len(argv)!=2):
        print("Invalid Number of Argument")
        exit()

    if(argv[1]=='-h' or argv[1]=='-H'):
        prefix("The Automation script is used to perform file automation")

    elif(argv[1]=='-u' or argv[1]=='U'):
        print("Usage : Name of Script")
        print("Example : Demo.py Satyam")
        exit()

    else:
        try:
            DirectoryTravel(argv[1])

        except Exception as E:
            prefix("Invalid Error :",E)

if __name__ == "__main__":
    main()