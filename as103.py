import numpy as np
n = int(input("enter n:"))
v = (n * (n**2 + 1)/2)/n**2
a=np.full(shape=(n,n), fill_value=v)
print(a)
