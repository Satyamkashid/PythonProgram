No=0
print("Enter the number :")
No=int(input())

for i in range(1,No,1):
    if(No % i==0):
        print(i)