import os
import threading

def task1(Value):
    print("PID of task1 :",os.getpid())
    print("Thread ID of first thread is :",threading.get_ident())

def task2(Value):
    print("PID of task2 :",os.getpid())
    print("Thread ID of second thread is :",threading.get_ident())


def main():
    print("PID of parent process is :",os.getpid())
    print("Thread ID of main thread is :",threading.get_ident())

    No=5
    t1 = threading.Thread(target=task1,args=(No,))
    t2 = threading.Thread(target=task2,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()