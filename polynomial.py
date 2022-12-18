#compute polynomial
import math
n=int(input("Enter degree of polynomial:"))
print("Enter",n+1,"coefficients:")    
ls=[]
for i in range (n+1):
      a=int(input())
      ls.append(a)
print("The coefficients are:")
print(ls)
x=int(input("Enter the value of x:"))
sum1=0
i=0
while (n>=0 and i<len(ls)):
          sum1+=ls[i]*pow(x,n)
          n-=1
          i+=1
print("The value of the polynomial at",x,"is:",sum1)
