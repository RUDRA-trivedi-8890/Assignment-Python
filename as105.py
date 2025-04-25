import numpy as np
import copy
n = str(input("enter strings sep by comaa:"))
n = n.split(",")
k= copy.deepcopy(n)
j= copy.deepcopy(n)
for i in range(len(n)):
    n[i] = np.char.center(n[i],width=15,fillchar='_')
print(*n)
for i in range(len(k)):
    k[i] = np.char.rjust(k[i],width=15,fillchar='_')
print(*k)
for i in range(len(j)):
    j[i] = np.char.ljust(j[i],width=15,fillchar='_')
print(*j)
