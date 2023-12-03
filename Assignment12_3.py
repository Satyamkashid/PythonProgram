import os
import psutil
import time
from sys import *

def ProcessDisplay(DirName):
    listprocess = []

    if not os.path.exists(DirName):
        try:
            os.mkdir(DirName)
        except:
            pass

    seperator = "-" * 100

    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(DirName,f"MarvellousLog_{current_time}.log")

    f = open(log_path,'w')
    f.write("Marvellous Infosystem Process Logger :" + current_time + "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid' , 'name' , 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write(" %s \n" % element)

    return listprocess

def main():
    print("----------Marvellous InfoSystem---------")

    print("Application name : ",argv[0])

    if(len(argv) !=2):
        print("Invalid Number of Argument")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is Used to record running Processes in Log File")
        exit

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsulutePathOfDirectory")
        exit

    try:
        listprocess = ProcessDisplay(argv[1])

        icnt = 0

        for elem in listprocess:
            icnt+=1
            print(elem)
        print("Number of Running Processes are : ",icnt)

    except Exception as E:
        print("Invalid Error : ",E)


if __name__ == "__main__":
    main()