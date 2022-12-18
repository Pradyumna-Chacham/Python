#Program to add two numbers from the user
import random
ls1=[]
for i in range (1,101):
    ls1.append(i)
print("Add the following numbers:")
x=random.choice(ls1)
print(x)
y=random.choice(ls1)
print(y)
a=x+y
z=int(input())
if (a==z):
    print("Congratulations!Correct answer.")
else:
    print("Wrong answer. Correct answer is:",a)
