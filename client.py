import marvellous
def main():
        value1=int(input("Enter first Number"))
        value2=int(input("Enter second Number"))
        Result=0

        Result=marvellous.Addition(value1,value2)
        print("Addition is",Result)

        Result=marvellous.Subtraction(value1,value2)
        print("Addition is",Result)

        Result=marvellous.Multiplication(value1,value2)
        print("Addition is",Result)

if __name__ == "__main__":
        main()