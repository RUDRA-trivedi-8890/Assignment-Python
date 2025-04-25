import numpy as np
a=np.zeros(shape=(8,8))
# a[0][0] = 1 #queen inserted at pos=(0,0)
k=0
j=0
for i in range(8):
    if(a[i][j]==1):
        i+=1
    else:
        if(k>3):
            a[i][(2*k+2)%8]=1
            k+=1
        else:
            a[i][(2*k+1)%8] = 1
            k+=1
print(a)            