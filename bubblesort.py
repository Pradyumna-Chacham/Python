#Bubble Sort
n=int(input("Enter how many elements you want to store in the list:"))
print("Enter",n,"elements:")
ls=[]
for i in range (n):
    x=int(input())
    ls.append(x)
print("List before sorting:")
print(ls)
#Bubble sort
for i in range(len(ls)):
    for j in range (len(ls)-i-1):
        if (ls[j]>ls[j+1]):
            ls[j],ls[j+1]=ls[j+1],ls[j]
print("List after sorting:")
print(ls)
