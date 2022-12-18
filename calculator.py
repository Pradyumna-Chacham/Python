#Program to design simple calculator
print ("Enter two numbers:")
a,b=int(input()),int(input())
print ("Enter operator:")
x=input()
if (x=='+'):
    c=a+b
    print("The sum of",a,"and",b,"is:",c)
elif(x=='-'):
    c=a-b
    print("The difference pf",a,"and",b,"is:",c)
elif(x=='*'):
    c=a*b
    print("The product of",a,"and",b,"is:",c)
elif(x=='/'):
    c=a//b
    print("The quotient when",a,"is divided by",b,"is:",c)
elif(x=='%'):
    c=a%b
    print("The remainder when",a,"is divided by",b,"is:",c)
else:
    print("Not a valid operator")
    
