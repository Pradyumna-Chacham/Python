#Number operations
n=int(input("Enter a number:"))
temp=n
sum1=0
product=1
while (n>0):
    r=n%10
    sum1+=r
    product*=r
    n=n//10
print("The sum of digits of",temp," is:",sum1)
print("The product of the digits of",temp,"is:",product)
b=temp
b=str(b)
print("The no.of digits in",temp,"is:",len(b))
    
