
Add= lambda No1,No2 : No1+No2

Sub = lambda No1,No2 : No1-No2

def Marvellous(Value1,Value2):
    Ans1=Add(Value1,Value2)
    Ans2=Sub(Value1,Value2)

    return Ans1,Ans2

def main():
   Arr=Marvellous(11,6)
   print("Addition is :",Arr[0])
   print("Subtraction is :",Arr[1])


    
if __name__ == "__main__":
    main()