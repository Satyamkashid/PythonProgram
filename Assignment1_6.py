# Program to check Number is Positive,Negative or zero

def ChkNo(No):
    if No>0:
        print(No,"is Positive")

    elif No<0:
        print(No,"is Negative")

    else:
        print(No,"is Zero")

def main():
    Value=11
    ChkNo(Value)

    Value = -8
    ChkNo(Value)

    Value = 0
    ChkNo(Value)

if __name__ == "__main__":
    main()