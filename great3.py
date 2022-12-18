#Program to find the largest of three numbers
print("Enter three numbers:")
a,b,c=input().split()
if ((a>b) and (a>c)):
    print (a,"is greatest")
elif (b>c):
    print (b,"is greatest")
else:
    print(c,"is greatest")
    
