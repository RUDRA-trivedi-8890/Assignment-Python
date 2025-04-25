class Node:
    def init(self):
        self.head=None
    def __init__(self,val):
        self.val = val
        self.next = None     
    def creatlist(self):
        m = int(input("enter number of node to make:"))
        for i in range(m):
            print("enter data of ",i+1,"th Node:")
            val = int(input())
            newnode = Node(val)
            newnode.next = None
            self.head=newnode
c=Node()
c.creatlist()
        
    