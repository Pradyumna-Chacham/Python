#Accept three digits and print all combinations of the three digits
a=int(input("Enter a digit:"))
b=int(input("Enter a second digit:"))
c=int(input("Enter a third digit:"))
print("The three combinations of the digits are:")
ls1=[]
ls1.append(a)
ls1.append(b)
ls1.append(c)
for i in range (3):
      for j in range (3):
          for k in range(3):
                  if (i!=j and j!=k and k!=i):
                      print(ls1[i],ls1[j],ls1[k])

