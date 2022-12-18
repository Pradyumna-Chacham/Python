#Read a date from the user and check its validity
print("Enter day:")
day=int(input())
print("Enter month:")
month=int(input())
print("Enter year:")
year=int(input())
print("Entered date is:",day,"/",month,"/",year)
#Checking for invalid date
if (month==1 or month==3 or month==5 or month == 7 or month==8 or month==10 or month==12):
    max1=31
elif (month==4 or month==6 or month==9 or month==11):
    max1=30
elif (month==2 and year%4==0 and year%100!=0 or year%400==0):
    max1=29
else:
    max1=28
if (day<1 or month<1 or year<1):
    print("Entered date is invalid")
if (day>31 or month>12):
    print("Entered date is invalid")
#Printing incremented date
elif (day==max1 and month!=12):
    day=1
    month+=1
    print("Incremented date is:",day,"/",month,"/",year)
elif (day==max1 and month==12):
    day,month,year=1,1,year+1
    print("Incremented date is:",day,"/",month,"/",year)
elif (day<max1):
    day=day+1
    print("Incremented date is:",day,"/",month,"/",year)
    
    
