import threading

def EvenList(list):
    Sum=0
    for i in list:
        if i % 2 ==0:
            Sum+=i
    print("Sum of Even Number is ",Sum)

def OddList(list):
    Sum=0
    for i in list:
        if i % 2 != 0:
            Sum+=i
    print("Sum of Odd Number is ",Sum)
    

def main():
    Data = []
    print("How Many Elements You Want in List")
    size = int(input())

    for i in range(size):
        print("Enter the Elements")
        number=int(input())
        Data.append(number)

    print(Data)

    t1 = threading.Thread(target=EvenList,args=(Data,))
    t2 = threading.Thread(target=OddList,args=(Data,))

    t1.start()
    t1.join()
    t2.start()

    
    t2.join()

if __name__ == "__main__":
    main()