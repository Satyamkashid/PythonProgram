def Minimim_List(list):
    smallest=list[0]
    for i in list:
        if i < smallest:
            smallest=i
    return(smallest)


def main():
    Data=[]
    print("Enter the number")
    size=int(input())

    for i in range(size):
        print("Enter the elements :")
        value=int(input())
        Data.append(value)
    print(Data)

    Ans=Minimim_List(Data)
    print("Smallest Number from list is :",Ans)
    
if __name__ == "__main__":
    main()