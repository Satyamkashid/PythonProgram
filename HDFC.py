class HDFC:
    ROI = 9.5   #class vairiable

    def __init__(self,Name,Amount):   #Constructor
        self.AccountHolder = Name
        self.Balance=Amount      #Instance Variable
        print("Welcome",self.AccountHolder)
        print("Account gets successfully created with initial balance :",self.Balance)

    def DisplayBalance(self):    #Instance Method
        print("Hello",self.AccountHolder)
        print("Your account balance is :",self.Balance)

    @classmethod
    def DisplayBankInfo(cls):    #Class Method
        print("Welcome to HDFC bank portal")
        print("Our bank is PVT LTD bank")
        print("We provide the rate of intrest on saving account is :",cls.ROI)

    @staticmethod
    def DisplayKYCInfo():
        print("Accordind to the rules of RBI you should provide below document for KYC")
        print("Your Adhar card")
        print("Your PAN card")
        print("Your Passport size photo")


    def Withdraw(self,Amount):   #Instance Method
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance=self.Balance-Amount
            print("Amount withdraw successfully...")

    def Deposit(self,Amount):   #Instance Method
        self.Balance = self.Balance + Amount
        print("Ammount deposited successfully...")

def main():
    print("ROI of HDFC bank is :",HDFC.ROI)

    HDFC.DisplayBankInfo()
    HDFC.DisplayKYCInfo()

    print("Creating new account....")
    Amit=HDFC("Amit",5000)    #__init__(100,"Amit",5000)

    print("Creating new account....")
    Saagar=HDFC("Sagar",3000)    #__init__(200,"Sagar",3000)

    print("Performing operation on OBJ1")
    Amit.Deposit(2000)
    Amit.DisplayBalance()

    Amit.Withdraw(1000)
    Amit.DisplayBalance()

    print("Performing Operation on Sagar's Account")
    Saagar.Deposit(4000)
    Saagar.DisplayBalance()

    Saagar.Withdraw(500)
    Saagar.DisplayBalance()



if __name__ == "__main__":
    main()