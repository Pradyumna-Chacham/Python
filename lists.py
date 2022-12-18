#Program to find average of list elements
n=int(input("Enter how many elements you want to store in the list:"))
ls=[]
evenls=[]
oddls=[]
print("Enter",n,"elements:")
for i in range (n):
    x=int(input())
    ls.append(x)
print("The list after adding elements:")
print(ls)
#Sum of list elements
sumlist=0
for i in ls:
    sumlist+=i
print("The sum of array elements:",sumlist)
#Average of list elements
average=sumlist//len(ls)
print("The average of array elements:",average)
#Maximum and minimum of list
print("The maximum of list:",max(ls))
print("The minimum of list:",min(ls))
#Even and odd elements of list
for i in ls:
    if (i%2==0):
        evenls.append(i)
    else:
        oddls.append(i)
print("The even elements of the list are:")
print(evenls)
print("The odd elements of the list are:")
print(oddls)
#List elements in reverse
print("List elements in reverse:")
print(ls[::-1])
