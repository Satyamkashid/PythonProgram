def Star(No):
    for i in range(No):
        for j in range(i,No):
            print("*",end=' ')
        print()

def main():
    print("Enter the Number :")
    Value=int(input())

    Ans=Star(Value)

if __name__ == "__main__":
    main()