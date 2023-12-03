from sys import*
import os 
import time

def DirectoryTravel(DirName):
    print("We are going to scan the directory :",DirName)

    for foldername,subfoldername,filename in os.walk(DirName):
        print("Curent folder name :",foldername)

        for subname in subfoldername:
            print("Sub Folder name is :",subname)

        for fname in filename:
            print(fname," : ",os.path.getsize(foldername+"/"+fname),"bytes")


def main():
    print("--------Automation script------")

    print("Nmae of the Script :",argv[0])

    if(len(argv)!=2):
        print("INvalid Number of Argument")
        exit()

    if(argv[1]=='-h' or argv[1]=='-H'):
        print("We are going to perform file automation")

    elif(argv[1]=='u' or argv[1]=='-U'):
        print("Usage :")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The Script took time to execute as ",endtime-starttime)

if __name__ == "__main__":
    main()
