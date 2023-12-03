
def Display(Name,Age,Marks=90):
    print("Nmae is",Name)
    print("Age is",Age)
    print("Marks are",Marks)

def main():
    print("Demonstration of keyword arguments")

    Display("Amit",25)
    Display("Sagar",21,78)


if __name__ == "__main__":
    main()