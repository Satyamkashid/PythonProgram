class BankAccount:
    ROI = 10.5
    def __init__(self):
        print("Enter Your Name")
        self.Name = str(input())

        print("Enter the Ammount")
        self.Amount = int(input())

    def Deposit(self):
        print("Enter the Ammount You Want to Deposit")
        Amt = int(input())
        self.Amount = self.Amount + Amt

        print("Total Ammount :",self.Amount)

    def Withdraw(self):
        print("Enter the Ammount You Want to Withdraw")
        Amt1 = int(input())
        if(Amt1 > self.Amount):
            print("Insufficient Balance")
        else:
            self.Amount = self.Amount - Amt1
            print("Total Ammount :",self.Amount)

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

    def Display(self):
        print("Hello",self.Name)
        print("Your account balance is :",self.Amount)

def main():
    print("How Many object You Want")
    obj1 = int(input())
    for i in range(obj1):

        obj1 = BankAccount()
        obj1.Deposit()
        obj1.Withdraw()
        print("Your Rate of Interest is :",obj1.CalculateInterest())
        obj1.Display()

if __name__ == "__main__":
    main()