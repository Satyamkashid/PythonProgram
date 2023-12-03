def Addition(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def Sub(No1,No2):
    Ans=0
    Ans=No1-No2
    return Ans

def main():
    print("Enter the first number")
    value1=int(input())

    print("Enter the second number")
    value2=int(input())

    Result=Addition(value1,value2)
    print("Addition is :",Result)

    Result=Sub(value1,value2)
    print("Subtraction is :",Result)

if __name__ == "__main__":
    main()