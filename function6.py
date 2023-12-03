def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

# function accept parameter and call another function from it and return multiple values

def Marvellous(Value1,Value2):

    Ans1 = Add(Value1,Value2)
    
    Ans2 = Sub(Value1,Value2)
    
    return Ans1,Ans2
    


def main():
   Arr=Marvellous(11,6)
   print("Addition is :",Arr[0])
   print("Subtraction is :",Arr[1])


    
if __name__ == "__main__":
    main()