#que using python
class Queue:
    l = []
    top  = -1
    n=0
    @classmethod
    def __init__(cls):
        cls.n = int(input("enter queue size:"))
    def enque(cls,val):
        if(cls.top==cls.n):
            print("queue over flow")
        cls.l.append(val)
        cls.top+=1
    def dequeue(cls):
        if(cls.top==-1):
            print("queue underflow!")
        x=cls.l.remove(cls.l[0])
        cls.top-=1
        return x
    def display(cls):
        print("your queue is::")
        for i in cls.l:
            print(i,end=" ")
q=Queue()
q.enque(50)
q.enque(48)
q.enque(46)
q.dequeue()
q.display()
        
        
        