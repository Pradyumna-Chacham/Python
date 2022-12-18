#Calculator
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
x=input("Enter operator:")
if (x=='+'):
    c=a+b
    print("The sum of ",a,"and",b,"is:",c)
elif (x=='-'):
    c=a-b
    print("The difference of ",a,"and",b,"is:",c)
elif(x=='*'):
    c=a*b
    print("The product of ",a,"and",b,"is:",c)
elif(x=='/'):
    c=a/b
    print("The quotient when",a,"is divided by ",b,"is:",c)
elif(x=='%'):
    c=a%b
    print("The remainder when",a,"is divided by ",b,"is:",c)
else:
    print("Not a valid operator")

    
