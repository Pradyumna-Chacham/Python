#Program to find prime numbers in the list
ls=[]
primels=[]
n=int(input("Enter how many elements you want to store in the list:"))
print("Enter",n,"elements:")
for i in range (n):
    x=int(input())
    ls.append(x)
#Printing list after adding elements
print("list after adding elements:")
print(ls)
#Checking for prime numbers
count=0
for i in ls:
    for j in range (2,n):
        if (i%j==0):
            count=1
        if (count==0):
            primels.append(i)
        if (count!=0):
            count=0
            
print("Prime numbers in the list are:")
print(primels)
