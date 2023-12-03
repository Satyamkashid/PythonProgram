
def main():
    try:

        print("Enter first Number")
        no1=int(input())

        print("Enter second Number")
        no2=int(input())

        Ans = 0

        Ans = no1 / no2

    except ZeroDivisionError as zobj:
        print("Divide by zero is not allowed",zobj)
        return

    except ValueError as obj:
        print("Invalid Input :",obj)
        return
    
    except Exception as zobj:
        print("Exception occured as",zobj)
        return
    
    finally:
        print("Thank You For Using the Application")

    print("Division is ",Ans)


if __name__ == "__main__":
    main()