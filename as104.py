import numpy as np
import math
n = int(input("enter number of points you want to add"))
l = []
for i in range(n):
    print("enter x axis of",i+1,"th point")
    x = int(input())
    print("enter y axis of",i+1,"th point")
    y = int(input())
    r = (x,y)
    l.append(r)
ans=[]
# polarconverter(l)
def polarconverter(l  ):
    for i in l:
        val = i[1]/i[0]
        theta = math.atan(val)
        r = (i[0]**2 + i[1]**2)**(0.5)
        p = (r,theta)
        ans.append(p)
polarconverter(l)
print(ans)
        

    
    
