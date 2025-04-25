#the love latter mystrey
n=int(input("enter number of test cases:"))
i,j=0,0
x=[]
while(i!=n):
    s=str(input("enter a string:"))
    while(j<len(s)//2):
        if(s[j]!=s[-1-j]):
            r=ord(s[0+j]) - ord(s[-1-j])
            if(r<0):
                r=-r
            x.append(r)
        j+=1
    i+=1
print(sum(x))