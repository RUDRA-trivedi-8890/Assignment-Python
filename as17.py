n=int(input("enter number of test cases:"))
pieces=[]
l=[]
for i in range(n):
    k=int(input("enter number of cuts:"))
    l.append(k/2)
    pieces.append(int(l[i]**2))
print(pieces)