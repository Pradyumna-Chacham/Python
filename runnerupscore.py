#hackerrank runner up score
arr=[]
n = int(input("Enter hwo many scores you want to read:"))
print ("Enter",n,"scores:")
for i in range (n):
    a=int(input())
    arr.append(a)
y=max(arr)
z=arr.count(y)
while (z>0):    
    for i in arr:
        if (i==y):
            arr.remove(i)            
    z=z-1
y=max(arr)
print(y)
    
