# def Maximum_List(list):
#     return max(list)

def Maximum_List(list):
    largest = list[0]
    for i in list:              
        if i > largest:
            largest = i
    return(largest)
    

def main():
    Arr=[]
    print("Enter the number :")
    size=int(input())

    for i in range(size):
        print("Enter elements :")
        value=int(input())

        Arr.append(value)
    print(Arr)

    Ans=Maximum_List(Arr)
    print("Maximum number from list is :",Ans)

if __name__ == "__main__":
    main()