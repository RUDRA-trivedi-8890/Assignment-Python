#bigger is greater'''
s1=str(input("enter thr string"))
s2=s1
list1=[]
list2=[]

for i in range(len(s1)-2):
    l1=list(s1)
    l2=list(s2)
    if(ord(s2[-1-i])> ord(s1[-2-i])):
        l1[-2-i],l1[-1-i] = l2[-1-i],l2[-2-i]
        s3="".join(l1)
        s4="".join(l2)
    if(s3>s4):
        break

if(s3==s4):
    print("no answer")
else:
    print(s3)

        