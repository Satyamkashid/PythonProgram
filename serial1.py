def fun(No):
    sum=0
    for i in range(100000):
        sum=sum+(No*No)
    return sum
def main():
    print("Demonstration of serial execution using singlee core")

    Result = []

    for No in range(10000):
        Result.append(fun(No))

if __name__ == "__main__":
    main()