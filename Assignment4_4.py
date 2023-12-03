from functools import reduce

ChkEven = lambda No : (No % 2 ==0)

Square = lambda No : (No * No)

Add = lambda No1,No2 : (No1+No2)

def main():
    Data=[]
    print("Enter the number of elements ")
    size=int(input())

    for i in range(size):
        print("Enter the elements")
        Value=int(input())
        Data.append(Value)

    print(Data)

    output = list(filter(ChkEven,Data))
    print("Output after filter",output)

    output1 = list(map(Square,output))
    print("Output after map",output1)

    output2 = reduce(Add,output1)
    print("Output after reduce",output2)


if __name__ == "__main__":
    main()