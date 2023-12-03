def Star(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            if j<=i:
                print(i,end=' ')
            else:
                print(j,end=' ')
        print()

def main():
    print("Enter the Number :")
    Value=int(input())

    Ans=Star(Value)

if __name__ == "__main__":
    main()