
class Arithmatic:
    def __init__(self,A,B):
        print("Inside Constructor")
        self.No1=A
        self.No2=B
    
    def Addition(self):
        Ans=0
        Ans=self.No1+self.No2
        return Ans
    
    def Subtraction(self):
        Ans=0
        Ans=self.No1-self.No2
        return Ans


def main():
    print("Enter the first number")
    value1=int(input())

    print("Enter the second number")
    value2=int(input())

    obj1=Arithmatic(value1,value2)

    Ret=obj1.Addition()
    print("Addition is :",Ret)

    Ret=obj1.Subtraction()
    print("Subtraction is :",Ret)


    print("Enter the first number")
    value1=int(input())

    print("Enter the second number")
    value2=int(input())

    obj2=Arithmatic(value1,value2)

    Ret=obj2.Addition()
    print("Addition is :",Ret)

    Ret=obj2.Subtraction()
    print("Subtraction is :",Ret)

if __name__ == "__main__":
    main()