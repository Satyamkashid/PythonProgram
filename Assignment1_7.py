# program to check whether the number is divisible by 5 or not 

def Divisible(No):
    if No % 5 == 0:
        print(True)

    else:
        print(False)

def main():
    Value=int(input("Enter the Number to Check Whether it is divisible by 5 or not"))
    Divisible(Value)

if __name__ == "__main__":
    main()