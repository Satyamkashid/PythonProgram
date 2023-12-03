# Program to add Numbers from user

def Add(No1,No2):
    Result=No1+No2
    return Result

def main():
    print("Enter the first Number")
    Value1 = int(input())

    print("Enter the second Number")
    Value2 = int(input())

    Ans=Add(Value1,Value2)
    print("Addition is :",Ans)


if __name__ == "__main__":
    main()