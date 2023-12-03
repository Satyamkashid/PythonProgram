from functools import reduce
def Add(A,B):
    return A+B

def main():
    Arr = []
    print("Enter the number :")
    size=int(input())

    print("Enter the elements :")
    for i in range(size):
       Value=int(input())
       Arr.append(Value)
    print(Arr)

    op=reduce(Add,Arr)
    print(op)

if __name__ == "__main__":
    main()