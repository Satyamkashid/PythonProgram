# program to check the number is even or odd

def ChkNum(No):
    if No % 2 == 0:
        print(No," is Even")
    else:
        print(No," is Odd")

def main():
    Value = 11
    ChkNum(Value)

    Value = 8
    ChkNum(Value)

if __name__ == "__main__":
    main()
    