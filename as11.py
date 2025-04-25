#Is Fibo
def fibomaker(n):
    l=[0,1]
    for i in range(n):
        l.append(l[1+i]+l[i])
    k=int(input("enter number that you want to check:"))
    if(k in l):
        print("isfebo")
    else:
        print("isnotfibo")
print("enter number of charcter in febo:")
n=int(input())
fibomaker(n)


