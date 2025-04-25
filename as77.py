class vector_2d:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y=  y
        self.z = z
    def magnitude(self):
        self.magni = (self.x**2 + self.y**2 + self.z**2)**(0.5)
        print("magnitude of these two vectoes is:",self.magni)
    def __mul__(self,other):
        x=vector_2d()
        x.x=self.x * other.x
        x.y=self.y * other.y
        x.z=self.z * other.z
        return x   
    def show(self):
        print(self.x,"i^ +",self.y,"j^")
class vector_3d(vector_2d):
    pass
v=vector_3d(10,5,10)
v.magnitude()

    
        
        