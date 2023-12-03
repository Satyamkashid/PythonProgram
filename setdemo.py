Set1={11,34.4,"hello",True}
print(Set1)

# print(Set1[1])    Not Allowed

for Value in Set1:
    print(Value)

# for i in range(len(Set1)):  Not Allowed
#     print(Set1[i])

Set2={11,78,89,11,78}
print(Set2)

Set2.add(101)
print(Set2)

Set2.remove(101)
print(Set2)

print("enter the value that you want to search in set")
No=int(input())
for Value in Set2:
    if(No==Value):
        print("Element is present")
        break

print(89 in Set2)