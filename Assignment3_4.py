# def main():
#     Data=[]
#     print("Enter the number")
#     size=int(input())

#     print("Enter the elements :")
#     for i in range(size):
#         value=int(input())
#         Data.append(value)
#     print(Data)

#     print("Enter the number to calculate the frequency of that number :")
#     Number=int(input())
#     cnt=0
#     for i in Data:
#         if Number==i:
#             cnt+=1
#     print(cnt)


# if __name__ == "__main__":
#     main()




def Freq(list,No):
    cnt = 0
    for i in list:
        if No == i:
            cnt+=1
    print(cnt)

def main():
    Data = []
    print("Enter the Number")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        value=int(input())
        Data.append(value)
    print(Data)

    print("Enter the Number to count the frequency ")
    num=int(input())
    Ans=Freq(Data,num)

if __name__ == "__main__":
    main()