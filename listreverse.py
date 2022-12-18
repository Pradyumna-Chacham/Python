#Program to swap elements in list?Reverse elemetns in list
n=int(input("Enter how many elements you want to store in the list:"))
ls=[]
print("Enter",n,"elements:")
for i in range (n):
    x=int(input())
    ls.append(x)
print("List before swapping:")
print(ls)
#Swapping list
for i in range (len(ls)//2):
    ls[i],ls[n-i-1]=ls[n-i-1],ls[i]
print("List after reversing:")
print(ls)
    
