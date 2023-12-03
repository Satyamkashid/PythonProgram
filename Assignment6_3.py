class Arithmetic:
    def __init__(self):
        print("Enter the Number")
        self.Value = int(input())

    def ChkPrime(self):
        for i in range(2,self.Value):
            if(self.Value % i ==0):
                return False
        else:
            return True
        
    def ChkPerfect(self):
        Sum=0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum+=i
        if(Sum == self.Value):
            print("Perfect")
        else:
            print("Not Perfect")

    def Factors(self):
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                print(i,end=' ')

    def SumFactors(self):
        sum=0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                sum+=i
        return sum

    
def main():
    print("How Many Times You Want to Perform the Operation")
    obj=int(input())
    for i in range(obj):
        obj=Arithmetic()
        print("Is The Number is Prime?", obj.ChkPrime())
        obj.ChkPerfect()
        obj.Factors()
        print()
        print("Sum of factors :", obj.SumFactors())

if __name__ == "__main__":
    main()