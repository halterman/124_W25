from circle import Circle
from point import Point
from shape import Shape
from rectangle import Rectangle
from person import Tool

def measure(obj: Shape) -> float:
    return obj.area()

r1 = Rectangle(Point(5, 10), 25, 8)

# This DOES work because a rectangle is a shape
print(measure(r1))

print(r1.width)

# This does not work because a tool is NOT a shape
# t1 = Tool(7)
# print(measure(t1))

# This DOES work because a circle is a shape
c1 = Circle(Point(0, 0), 15)
print(measure(c1))