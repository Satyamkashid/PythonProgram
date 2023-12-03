import os
def main():
    print("Enter the name of file")
    file_name = input()

    if os.path.exists(file_name):
        fobj = open(file_name,"r")
        if fobj:
            print("Successfully opened")
            Data = fobj.read()
            print("Data from file is :",Data)
            fobj.close()
        else:
            print("Unable to open file")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()