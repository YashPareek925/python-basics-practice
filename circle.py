# Define a Circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        self.area=3.14*self.radius**2
        print("Area of circle",self.area)

    def Perimeter(self):
        self.perimeter=2*3.14*self.radius
        print("Perimeter of cirlce:- ",self.perimeter)

r=float(input("Enter the radius:- "))
c1=Circle(r)
c1.Area()
c1.Perimeter()