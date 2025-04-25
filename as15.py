#pangram
dict={}
alpha=range(97,123,1)
#beeta=range(97,123,1)
count=0
s=str(input("enter a sentance:"))
s=s.lower()
for i in alpha:
    if(chr(i).isalpha()):
        dict[chr(i)]=dict.get(chr(i),0) + 1 if chr(i) in s else dict.get(chr(i),0)
if(0 in dict):
    print("not pangram")
else:
    print("pangram")