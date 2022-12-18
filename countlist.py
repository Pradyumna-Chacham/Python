#Count the no.of times a number occurs in a list
n=int(input("Enter how many numbers you want to add to the list:"))
print("Enter",n,"numbers:")
ls=[]
for i in range(n):
      x=int(input())
      ls.append(x)
target=int(input("Enter which number's occurence you want to check:"))
count=0
"""
for i in range (len(ls)):
      if (ls[i]==target):
          count+=1
print(target,"occurs",count,"times in the list.")
"""
y=ls.count(target)
print(target,"occurs",y,"times in the list")
