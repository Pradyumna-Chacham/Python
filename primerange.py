#program to print prime numbers in a range
x=int(input("ENter lower limit of range:"))
y=int(input("ENter upper limit of range:"))
print("Prime numbers between",x,"and",y,"are:")
for n in range(x,y+1):
        for i in range(2,n):
                if (n%i==0):
                        break
        else:
                print(n)
        
