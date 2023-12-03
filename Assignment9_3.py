import sys
import shutil

def FileCopy(fname,File_name):
    print("Contents of ",fname,"copied into",File_name)
    shutil.copy(fname,File_name)
    


def main():
    if(len(sys.argv) != 2):
        print("Invalid number of argument")
        exit()
    else:
        fname = sys.argv[1]
        file_name = "demo.txt"
        FileCopy(fname,file_name)
        
if __name__ == "__main__":
    main()