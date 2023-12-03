def SumFactors(Value):
    Sum=0
    for i in range(1,Value):
        if(Value % i == 0):
            Sum += i
            print(i,end=' ')
    print()
    print("Addition of Factors is ",Sum)

def main():
    No=0
    print("Enter the Number :")
    No=int(input())
    SumFactors(No)
if __name__== "__main__":
    main()



