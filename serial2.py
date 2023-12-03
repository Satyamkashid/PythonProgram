import time

def fun(No):
    sum=0
    for i in range(100000):
        sum=sum+(No*No)
    return sum

def main():
    print("Demonstration of serial execution using singlee core")

    starttime = time.time()

    Result = []

    for No in range(10000):
        Result.append(fun(No))

    endtime = time.time()
    print("Time required to execute the application is :",endtime-starttime)

if __name__ == "__main__":
    main()