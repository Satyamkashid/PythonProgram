import multiprocessing
import os

def task1(Value):
    print("Executing the first task...")
    for i in range(Value):
        print("Task1 :",i)

def task2(Value):
    print("Executing the second task...")
    for i in range(Value):
        print("Task2 :",i)


def main():
    print("Demontration of Multiprocessing")

    print("PID of running process is :",os.getpid())

    No1=5
    No2=8
    p1 = multiprocessing.Process(target=task1,args=(No1,))
    p2 = multiprocessing.Process(target=task2,args=(No2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()