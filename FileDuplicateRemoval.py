from sys import*
import os
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x) > 1,dict1.values()))

    icnt = 0
    ifound = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >=2:
                    os.remove(subresult)
                    ifound+=1
            icnt = 0
        print("Number of deleted files :",ifound)
    else:
        print("No Duplicate files found")

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) >0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}

    if exists :
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is :"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:                   #Duplicate
                    dups[file_hash].append(path)

                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")

def printResults(dict1):
    results = list(filter(lambda x: len(x) >1,dict1.values()))    #No of files greater than one

    if len(results) > 0:
        print("Duplicate Found")
        print("The following file are duplicate")
        for result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
    else:
        print("No Duplicate Found")

def main():
    print("----Marvellous Infosystem by Piyush Khairnar----")

    print("Application name :"+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or (argv[1]=='-H'):
        print("This Script is used to traverse specific directory")
        exit()
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory Extension")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print("Took %s seconds to evaluate " %(endTime-startTime))

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception as E:
        print("Error : Invalid Input",E)

if __name__ == "__main__":
    main()
