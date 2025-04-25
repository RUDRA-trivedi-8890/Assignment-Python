class shape:
    def area(self,a,b=0):
        if(b==0):
            area = 3.14 * (a**2)
            print("area of circle is",area)
        else:
            area = a*b
            print("area of rectangle is ",area)
    def perimeter(self,a,b=0):
        if(b==0):
            perimeter = 2*3.14*a
            print("perimeter of circle is",perimeter)
        else:
            perimeter = 2*(a+b)
            print("perimeter of rectangle is",perimeter)
class circle(shape):
    def __init__(self):
        rad = int(input("enter rad of circle:"))
        print("Enter 1 for Area")
        print("Enter 2 For Perimeter")
        n = int(input())
        if(n==1):
            super().area(rad)
        else:
            super().perimeter(rad)
class rectangel(shape):
    def __init__(self):
        print("enter length and bredth of rectangle")
        len = int(input())
        bre = int(input())
        print("Enter 1 for Area")
        print("Enter 2 For Perimeter")
        n = int(input())
        if(n==1):
            super().area(len,bre)
        else:
            super().perimeter(len,bre)
c=circle()
        