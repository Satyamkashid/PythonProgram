import sys

def main():
    print("Recursion limit is ",sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("Recursion Limit is ",sys.getrecursionlimit())
    
if __name__ == "__main__":
    main()
