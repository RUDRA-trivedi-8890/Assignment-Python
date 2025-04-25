#rock-paper scissor
import random
class rock_paper:
    def __init__(self):
        self.k=int(input("enter number of rounds"))
        self.game()
    def game(self):
        user=0
        cmpt=0
        m={"rock":1,"scisor":2,"paper":3}
        choices=["scisor","paper","rock"]
        n=random.choice(choices)
        if(n=="rock"):
            m[n]=3
            m["paper"]=4
            m["scisor"]=2
        elif(n=="paper"):
            m[n]=5
            m["rock"]=4
            m["scisor"]=5
        else:
            m[n]=5
            m['paper']=6
            m["rock"]=9
        for i in range(self.k):
            s=str(input("enter your choice:"))
            print("cmpt=",n)
            if(m[s]>m[n]):
                user+=1
            else:
                cmpt+=1
        if(user>cmpt):
            print("winner is user")
        elif(user==cmpt):
            print("match draw")
        else:
            print("winner is user")
s=rock_paper()
            
           
            
            