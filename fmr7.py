
Add = lambda No1,No2 : No1+No2
ChkEven = lambda No : (No % 2 ==0)
Increase = lambda No : (No+2)

# Task : Name of Functions
# Elements : Elements of Data elements
def filterX(Task,Elements):
    Result=[]
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result=[]
    for no in Elements:
        Ret=(Task(no))
        Result.append(Ret)
    return Result

def reduceX(Task,Elements):
    Sum=0
    for no in Elements:
        Sum=Task(Sum,no)
    return Sum


def main():
    Data = []
    print("Enter number of elements")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    output = list(filterX(ChkEven,Data))
    print("Output after filter",output)

    output1 = list(mapX(Increase,output))
    print("Output after map",output1)

    output2 = reduceX(Add,output1)
    print("Output after reduce",output2)


if __name__ == "__main__":
    main()