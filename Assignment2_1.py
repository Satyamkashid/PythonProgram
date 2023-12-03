import Arithmetic

def main():
    print("Enter frist Number :")
    Value1=int(input())

    print("Enter second Number :")
    Value2=int(input())

    Ans=Arithmetic.Add(Value1,Value2)
    print("Addition is :",Ans)

    Ans=Arithmetic.Sub(Value1,Value2)
    print("Subtraction is :",Ans)

    Ans=Arithmetic.Mul(Value1,Value2)
    print("Multiplication is :",Ans)

    Ans=Arithmetic.Div(Value1,Value2)
    print("Division is :",Ans)

if __name__ == "__main__":
    main()
