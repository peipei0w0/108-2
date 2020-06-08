from GeometricObject import GeometricObject
from Circle import Circle
from Rectangle import Rectangle

c_radius = int(input())
r_width = int(input())
r_height = int(input())
c_color = str(input())
c_filled = bool(input())
r_color = str(input())
r_filled = bool(input())

c = Circle(c_radius,c_color,c_filled)
r = Rectangle(r_width,r_height,r_color,r_filled)

print("Circle:")
print("Radius is ", c.getRadius())
print("Diameter is ", c.getDiameter())
print("Area is ", c.getArea())
print("Perimeter is ", c.getPerimeter())
print("color: ", c.getColor(), " and filled: ", c.isFilled())
print()

print("Rectangle:")
print("Width is ", r.getWidth())
print("Height is ", r.getHeight())
print("Area is ", r.getArea())
print("Perimeter is ", r.getPerimeter())
print("color: ", r.getColor(), " and filled: ", r.isFilled())