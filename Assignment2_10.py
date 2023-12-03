def DigitSum(No):
    Sum=0
    while(No>0):
        Sum=Sum + No % 10
        No = No // 10
    return Sum

def main():
    print("Enter the number")
    Value=int(input())
    Result=DigitSum(Value)
    print("Addition of digit ",Result)

if __name__ == "__main__":
    main()