N = int(input())
ls=[]
for i in range (N):
    command=input()
    a=[]
    a=command.split(" ")
    if (a[0]=="print"):
        print(ls)
    if (a[0]=="remove"):
        del ls[a[1]]
    if (a[0]=="append"):
        ls.append(a[1])
    if (a[0]=="sort"):
        ls.sort()
    if (a[0]=="pop"):
        ls.pop(ls[len(ls)-1])
    if (a[0]=="reverse"):
        ls.reverse()
    if (a[0]=="insert"):
        y=int(a[1])
        ls[y]=a[2]
            
