class Employ:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __add__(self,other):
        return (self.salary + other.salary)
    def __sub__(self,other):
        return (self.salary - other.salary)
    def __eq__(self, other):
        return (True if self.salary==other.salary else False)
    def __lt__(self, other):
        return (True if self.salary<other.salary else False)
    def __le__(self, other):
        return (True if self.salary<=other.salary else False)
    def __gt__(self, other):
        return (True if self.salary>other.salary else False)
    def __ge__(self, other):
        return (True if self.salary>=other.salary else False)
e1 = Employ("manthan",150)
e2 = Employ("pd",120)
x = e1==e2
print(x)