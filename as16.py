#xor value
l=int(input("enter left value:"))
r=int(input("enter right value:"))
xor=[]
for i in range(l,r+1):
    for j in range(l,r+1):
        x=i ^ j
        xor.append(x)
print(max(xor))