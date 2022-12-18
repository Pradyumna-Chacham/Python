n=int(input())
ls=[]

for _ in range(n):
    name = input()
    score = float(input())
    a=[]
    a.append(name)
    a.append(score)
    ls.append(a)
min1=ls[0][1]
print("Minimum before removing:",min1)
print("List before removing minimum:",ls)
for i in range (n):
    if (ls[i][1]<min1):
        min1=ls[i][1]
for i in range (n):
    if (ls[i][1]==min1):
        break
del ls[i][0]
del ls[i][1]
"""
print("List after removing minimum",ls)
min2=[]
for i in range (n):
    x=ls[i][1]
    min2.append(x)
print("list of marks:",min2)
"""
min2=ls[0][1]
for i in range (n):
    if (ls[i][1]<min2):
        min2=ls[i][1]
for i in range (n):
    if (ls[i][1]==min2):
        print(ls[i][0])
