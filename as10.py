#to find digital mode
num=int(input("enter a number"))
n=num
l=[]
def degitalmodefinder(n):
    while(n!=0):
        r=n%10
        n=n//10
        l.append(r)
    g=sum(l)
    l.clear()
    #print(g)
    if(g<10):
        print("the digitalroot is",g)
    else:
       degitalmodefinder(g)
degitalmodefinder(num)


        
    
    
