#armstrong,amicable and strong number
#Armstrong number
import math
n=int(input("Enter a number:"))
count=0
temp=n
#Counting digits of number
while (n>0):
    count+=1
    n=n//10
n=temp
#Checking whether armstrong number or not
sum1=0
while (n>0):
    r=n%10
    sum1+=pow(r,count)
    n=n//10
if (sum1==temp):
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")
#Amciable number
print("Enter two numbers:")
x,y=int(input()),int(input())
ls1=[]
ls2=[]
sum2=0
sum3=0
#Adding factors of one number into a list
for i in range (1,x):
    if (x%i==0):
        ls1.append(i)
for i in range (1,y):
    if (y%i==0):
        ls2.append(i)
#Sum of factors
for i in ls1:
    sum2+=i
print(sum2)
for i in ls2:
      sum3+=i
print(sum3)
if (sum2==y and sum3==x):
      print(x,"and",y,"are amicable numbers.")
else:
    print(x,"and",y,"are not amicable numbers.")
#Strong number
n=int(input("Enter a number:"))
sum4=0
temp=n
while (n>0):
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact*=i
    sum4+=fact
    n=n//10
if (sum4==temp):
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
    
    
