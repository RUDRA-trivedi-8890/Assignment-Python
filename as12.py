#utopian tree
n=int(input("enter number of test cases;"))
l=[]
k=1
height=1
for i in range(n):
    print("enter value of cycles in",i+1,"th test:")
    r=int(input())
    l.append(r)
for j in range(len(l)):
    for i in range(l[j]):
        if(i%2!=0):
            height=height+1
            print("height after",k,"th cycle is:",height)
            k+=1
        else:
            height*=2
            print("height after",k,"th cycle is:",height)
            k+=1
    height=1
    print("for n=",l[j])