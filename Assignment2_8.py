def Star(No):
    for i in range(No):
        p=1
        for j in range(i+1):
            print(p,end=' ')
            p+=1
        print()

def main():
    print("Enter the Number :")
    Value=int(input())

    Ans=Star(Value)

if __name__ == "__main__":
    main()