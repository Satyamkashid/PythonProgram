# program to accept number from user and print that number of stars in line 

def Star(No):
    for i in range(No):       #for _ in range(No) is also aloud
        print("*", end=' ')




def main():
    print("Enter the Number")
    Value = int(input())
    Ans= Star(Value)

if __name__ == "__main__":
    main()