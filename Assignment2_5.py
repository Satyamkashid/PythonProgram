def ChkPrime(No):
    for i in range(2,No):
        if No % i == 0:
            print("Not Prime")
            break
    else:
        print("It is Prime")

def main():
    print("Enter the Number")
    Value=int(input())

    ChkPrime(Value)

if __name__ == "__main__":
    main()