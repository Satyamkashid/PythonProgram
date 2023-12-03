from functools import reduce

def ChkEven(No):
    if No % 2 == 0:
        return True
    else:
        return False
    
def Increase(No):
    return No+2

def Add(A,B):
    return A+B    

def main():
    Data = [5,4,9,8,12,13,17,18]
    print(Data)

    output = list(filter(ChkEven,Data))
    print(output)

    output1 = list(map(Increase,output))
    print(output1)

    output2 = reduce(Add,output1)
    print(output2)

if __name__ == "__main__":
    main()