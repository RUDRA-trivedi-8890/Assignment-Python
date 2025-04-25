import numpy as np
import pandas as pd

def f(x):
    return x**3 - x -2
a=1
b=2

max_iter = 1000
def bisection_method(a,b,max_iter):
    if f(a)*f(b) < 0:
        for i in range(max_iter):
              c = (a+b)/2
              if(f(c)==0):
                return c
              elif(f(c)*f(a)<0):
                  b=c
              elif(f(b)*f(c)<0):
                  a=c
    else:
        print("root not found")
        
ans = bisection_method(a,b,max_iter)
print(ans)
    
    
    