class Demo:
    def __init__(self,Value1,Value2):    #Constructur
        print("Inside init method")
        self.No1=Value1
        self.NO2=Value2

    def Display(self):
        print("Value of No1 :",self.No1)
        print("Value of No2 :",self.NO2)


def main():
    print("Demonstration of Object Orientation")

    obj1=Demo(10,20)    #__init__(100(address means self),10,20)
    obj2=Demo(11,21)    #__init__(200(address means self),11,21)

    obj1.Display()
    obj2.Display()


if __name__ == "__main__":
    main()