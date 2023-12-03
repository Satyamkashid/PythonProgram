def fun(No):
    sum=0
    for i in range(100000):
        sum=sum+(No*No)
    return sum
def main():
    print("Demonstration of serial execution using singlee core")

    ret = fun(10)

    print(ret)

if __name__ == "__main__":
    main()