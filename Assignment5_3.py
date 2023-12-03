class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        print("Enter the value1:")
        self.Value1=int(input())

        print("Enter the value2:")
        self.Value2=int(input())

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    
def main():
    print("Enter How Many time you want to perform Operation")
    obj=int(input())
    for i in range(obj):

        obj=Arithmetic()

        obj.Accept()

        add=obj.Addition()
        sub=obj.Subtraction()
        mul=obj.Multiplication()
        div=obj.Division()

        print("Addition is :",add)
        print("Subtraction is :",sub)
        print("Multiplication is :",mul)
        print("Division is :",div)

if __name__ == "__main__":
    main()

    


