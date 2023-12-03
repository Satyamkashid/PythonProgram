import marvellous_fmr

Add = lambda No1,No2 : No1+No2
ChkEven = lambda No : (No % 2 ==0)
Increase = lambda No : (No+2)

def main():
    Data = []
    print("Enter number of elements")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    output = list(marvellous_fmr.filterX(ChkEven,Data))
    print("Output after filter",output)

    output1 = list(marvellous_fmr.mapX(Increase,output))
    print("Output after map",output1)

    output2 = marvellous_fmr.reduceX(Add,output1)
    print("Output after reduce",output2)


if __name__ == "__main__":
    main()