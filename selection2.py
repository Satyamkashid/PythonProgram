def CheckEven(Value):
    Result = Value % 2
    if(Result==0):
        print("Number is Even")
    else:
        print("Number is Odd")

def main():
    No=0
    print("Enter the Number :")
    No=int(input())

    CheckEven(No)

if __name__ == "__main__":
    main()