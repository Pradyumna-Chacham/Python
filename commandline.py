#PRogram to read a set of numbers from the command line and add and print those numbers
import sys
n=len(sys.argv)
print("Total arguments passed:",n)
print("Arguments passed:")
#Printing arguments
for i in range (1,n):
    print(sys.argv[i],end=" ")
#Adding numbers in commandline
sum=0
for i in range(1,n):
    sum+=int(sys.argv[i])
print("Sum of command line arguments:",sum)

