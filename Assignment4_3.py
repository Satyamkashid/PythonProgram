from functools import reduce

Mul = lambda No1,No2 : No1*No2

Greater = lambda No : (No>=70 and No <=90)

Increase = lambda No : (No+10)

def main():
    Data = []
    print("Enter number of elements")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    output = list(filter(Greater,Data))
    print("Output after filter",output)

    output1 = list(map(Increase,output))
    print("Output after map",output1)

    output2 = reduce(Mul,output1)
    print("Output after reduce",output2)


if __name__ == "__main__":
    main()