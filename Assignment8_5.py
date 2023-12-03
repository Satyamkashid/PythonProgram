def RecursiveFactorial(no):
    if no == 0 or no == 1:
        return 1
    else:
        return no * RecursiveFactorial(no - 1)

def main():
    try:
        print("Enter the Number")
        num = int(input())
    
        result = RecursiveFactorial(num)
        print(result)

    except ValueError as zobj:
        print("Invalid Input")

if __name__ == "__main__":
    main()

