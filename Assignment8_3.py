def Display(i):
    if i>=1:
        print(i)
        i-=1
        Display(i)

def main():
    Display(5)

if __name__ == "__main__":
    main()