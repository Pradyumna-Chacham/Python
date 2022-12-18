#Program to check whether a given number is an armstrong number or not
n=int(input("Enter a number:"))
temp=n
count=0
sum1=0
r=0
while (n>0):
    n=n//10
    count+=1
n=temp
temp=n
while (n>0):
    r=n%10
    sum1+=(r**count)
    n=n//10
if (sum1==temp):
    print(temp,"is an armstrong number:")
else:
    print(temp,"is not an armstrong number:")
    
