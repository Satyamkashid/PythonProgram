#  Function defines another function inside it and return as its return value

def Marvellous():   #0x200
    def Add(A,B):   #0x100
        return A+B
    
    return Add      #return 0x100

def main():         #0x300
    Ret=Marvellous()    #0x200()
    Ans=Ret(10,8)       #0x100(10,8)
    
    print("Addition is :",Ans)

if __name__ == "__main__":
    main()      #0x300