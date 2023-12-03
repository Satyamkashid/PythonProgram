import os
import psutil
import time
from sys import *
import os 

def ProcessDisplay(log_dir):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-" * 80

    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")  # Format the timestamp
    log_path = os.path.join(log_dir, f"MarvellousLog_{current_time}.log")  # Use underscores instead of spaces and remove colons

    f = open(log_path,'w')
    f.write(seperator + "\n")
    f.write("Marvellous Infosystem Process Logger :" + current_time + "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo);
        
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("------Marvellous Infosystem by Piyush Khairnar------")

    print("Application name :"+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or (argv[1]=='-H'):
        print("This Script is used log record of running process")
        exit()
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid input")  

    except Exception as e:
        print("Error : Invalid Input",e)

if __name__ == "__main__":
    main()