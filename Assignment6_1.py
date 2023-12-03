class BookStore:
    NoOfBooks = 0
    def __init__(self):
        self.Name = str(input("Enter the Name of Book"))
        self.Author = str(input("Enter the name of Author"))
        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.Name, "by", self.Author,"No of Books :",BookStore.NoOfBooks)

def main():
    obj1=BookStore()
    obj1.Display()
    print()
    obj2 = BookStore()
    obj2.Display()

if __name__ == "__main__":
    main()