class Node:
    list =[]
    @classmethod
    def __init__(cls):
        n = int(input("enter Number of Node you want to make:"))
        for i in range(n):
            cls.list.append(None)
    def insertion(cls):
        print("Enter where you want to insert")
        n =int(input())
        if(n<0 and n>len(cls.list)):
            print("wrong position")
            exit
        else:
            x = int(input("value of Node:"))
            cls.list[n-1] = x
    def deletion(cls):
        print("Enter position to delete")
        n = int(input())
        if(n<1 and n>len(cls.list)):
            cls.list.pop(n-1)
    def display(cls):
        for i in cls.list:
            print(i)
N = Node()
N.insertion()
N.display()
        
        
    