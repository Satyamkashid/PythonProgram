def Addition(No1,No2):
    Redult=0
    Result=No1+No2
    return Result
def main():
    value1=int(input("Enter the first number"))
    value2=int(input("Enter the second number"))
    Answer=0
    Answer=Addition(value1,value2)
    print("Addition is :",Answer)
main()