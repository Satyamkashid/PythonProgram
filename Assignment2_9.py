def Count_Digit(No):
    Length=len(str(No))
    print(Length)

def main():
    print("Enter the Number")
    Value=int(input())
    Count_Digit(Value)

if __name__ == "__main__":
    main()