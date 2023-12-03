import threading

def small(name):
    cnt=0
    for i in name:
        if i.islower():
            cnt+=1
    print("Total Number of small character are",cnt)

def capital(name):
    cnt=0
    for i in name:
        if i.isupper():
            cnt+=1
    print("Total Number of capital letter are ",cnt)

def digit(name):
    cnt = 0
    for i in name:
        if i.isdigit():
            cnt+=1
    print("Total Number of Digit are ",cnt)

def main():
    print("Enter the Name")
    name=str(input())

    t1 = threading.Thread(target=small,args=(name,))
    t2 = threading.Thread(target=capital,args=(name,))
    t3 = threading.Thread(target=digit,args=(name,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()