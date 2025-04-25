#sherlok and squres
import math
n=int(input("enter number of test cases:"))
count=0
for i in range(n):
    a=int(input("enter opening range:"))
    b=int(input("enter closing range"))
    for i in range(a,b+1,1):
        r=math.sqrt(i)
        if(int(r)==r):
            count+=1
        else:
            continue
print("number of squre integers is ",count)
        