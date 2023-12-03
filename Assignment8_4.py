
def RecursiveSum(no):
    if no < 10:
        return no
    last_digit = no % 10
    rest_of_digits = no // 10
    return last_digit + RecursiveSum(rest_of_digits)
    
def main():
    try:

        print("Enter the Number :")
        num=int(input())
    except ValueError as zobj:
        return

    result = RecursiveSum(num)
    print(result)

    
    

if __name__ == "__main__":
    main()
        