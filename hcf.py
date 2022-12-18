#HCF
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
hcf=0
if (a<b):
    for x in range (a,b):
        if (a%x==0 and b%x==0):
            hcf=x
else:
    for x in range (b,a):
        if (a%x==0 and b%x==0):
            hcf=x
print("HCF of",a,"and",b,"is:",hcf)
