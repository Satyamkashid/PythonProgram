def Display(Name,Age,Marks):
    print("Nmae is",Name)
    print("Age is",Age)
    print("Marks are",Marks)

def main():
    print("Demonstration of keyword arguments")

    Display(Name="Amit",Age=25,Marks=89)
    Display(Name="Sagar",Age=21,Marks=78)


if __name__ == "__main__":
    main()