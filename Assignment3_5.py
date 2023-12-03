import MarvellousNum
def main():
    Data = []
    print("Enter the number")
    size=int(input())

    for i in range(size):
        print("Enter the elements")
        value=int(input())
        Data.append(value)
    print(Data)

    print("Prime Numbers from list are :")
    Ans=[]
    for num in Data:
        if MarvellousNum.ChkPrime(num):
            Ans.append(num)
    print(Ans)

if __name__ == "__main__":
    main()