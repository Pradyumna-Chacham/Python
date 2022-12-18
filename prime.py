#Program to find if a given number is prime or not
n=int(input("Enter a number:"))
c=0
for i in range (2,(n//2)+1):
    if (n%i==0):
        c+=1
        break
if (c!=0):
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")
        
