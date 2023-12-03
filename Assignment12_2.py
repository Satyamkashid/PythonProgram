import psutil
import sys

def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess


def main(process_name):
    print("Marvellous Infosystem : Python Automation & Machine Learning")

    print("Process Monitor")

    listprocess = ProcessDisplay()

    icnt = 0

    for elem in listprocess:
        icnt+=1
        print(elem)

    print("Number of Running Process are :",icnt)

    # Check if the entered process name is running
    is_running = False
    for elem in listprocess:
        if elem['name'] == process_name:
            print(f"{process_name} is running with PID {elem['pid']}.")
            is_running = True
            break
    
    if not is_running:
        print(f"{process_name} is not running.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <process_name>")
    else:
        process_name = sys.argv[1]
        main(process_name)