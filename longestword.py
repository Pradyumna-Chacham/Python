#Return longest word
n=int(input("Enter how many words you want to add to the lsit:"))
print("Enter",n,"words:")
ls=[]
for i in range(n):
    x=input()
    ls.append(x)
max=len(ls[0])
for i in range(len(ls)):
       if (max<len(ls[i])):
        max=len(ls[i])
for i in ls:
    if(max==len(i)):      
        print("The longest string is:",i,"with length",max)
