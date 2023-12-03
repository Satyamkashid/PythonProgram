def Add(a,b):
    return a+b

# function accept parameter and call another function 

def Marvellous(FPTR):
    print(type(FPTR))
    print(FPTR)
    Ans=FPTR(11,7)
    print("Addition is :",Ans)
    


def main():
  Marvellous(Add)


    
if __name__ == "__main__":
    main()