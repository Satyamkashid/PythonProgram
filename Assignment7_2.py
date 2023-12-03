import threading
def EvenFactor(Value):
    Sum=0
    for i in range(1,Value):
        if(Value % i == 0) and (i % 2 == 0):
            Sum+=i
    print("Sum of Even Factor :",Sum)


def OddFactor(Value):
    Sum=0
    for i in range(1,Value):
        if(Value % i == 0) and (i % 2 != 0):
            Sum+=i
    print("Sum of Odd Factor :",Sum)

def main():
    print("Enter The Number :")
    Value = int(input())

    t1 = threading.Thread(target=EvenFactor,args=(Value,))
    t2 = threading.Thread(target=OddFactor,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
    