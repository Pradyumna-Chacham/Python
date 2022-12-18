#Linear search
n=int(input("Enter how many elements you want to store in the list:"))
print("Enter",n,"elements:")
ls=[]
for i in range (n):
    x=int(input())
    ls.append(x)
target=int(input("Enter element which you want to find:"))
for i in range(len(ls)):
           if (ls[i]==target):
               print(target," found at position",i+1)
if target not in ls:
    print("Element not found")
