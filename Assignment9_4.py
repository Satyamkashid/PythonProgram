import filecmp
from sys import *

def FileCompare(fname1,fname2):
    fobj1 = open(fname1,"rb")
    fobj2 = open(fname2,"rb")

    if(fobj1.read == fobj2.read):
        print("Success")
    else:
        print("Failure")

def main():
    if(len(argv) !=3):
        print("Invalid Number of Argument")
    else:
        FileCompare(argv[1],argv[2])


if __name__ == "__main__":
    main()