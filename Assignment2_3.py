def Factorial(No):
   fact=1
   for i in range(1,No+1):
      fact=fact*i
   return fact 


def main():
    print("Enter the Number")
    value=int(input())
    Ans=Factorial(value)
    print("Factorial of a number is ",Ans)

if __name__ == "__main__":
    main()