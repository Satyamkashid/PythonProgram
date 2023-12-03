
def Display(i):
    if i<=5:
        print("*",end=' ')
        i+=1
        Display(i)

def main():
    Display(1)

if __name__ == "__main__":
    main()