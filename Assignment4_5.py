from functools import reduce

def Prime(No):
    for i in range(2,No):
        if No % i == 0:
            return False
    else:
        return True

Mul = lambda No : (No * 2)

def main():
    Data = []
    print("Enter number of elements")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    output = list(filter(Prime,Data))
    print("Output after filter",output)

    output1 = list(map(lambda No : (No * 2),output))
    print("Output after map",output1)

    output2 = reduce(lambda x, y: x if x > y else y,output1)
    print("Output after reduce",output2)


if __name__ == "__main__":
    main()