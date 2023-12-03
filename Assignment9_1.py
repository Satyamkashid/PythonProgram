import os
def main():
    print("Enter the name of file you want to check")
    file_name = input()
    exist = os.path.exists(file_name)
    if exist:
        print("File exist")
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()

