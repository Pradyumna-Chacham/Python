#Program to print the ascending order of three numbers
print("Enter three numbers:")
a,b,c=int(input()),int(input()),int(input())
if (a>b):
    if(a>c):
        if(b>c):
            print("The ascending order is:",c,b,a)
        else:
            print("The ascending order is:",b,c,a)
    else:
        print("The ascending order is:",b,a,c)

else:
    if (b>c):
        if(a>c):
            print ("The ascending order is:",c,a,b)  
        else:
            print ("The ascending order is:",a,c,b)
    else   :
         print ("The ascending order is:",a,b,c)
