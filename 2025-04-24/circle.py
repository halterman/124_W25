from shape import Shape
from point import Point

class Circle(Shape):
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius * self.radius
    
    def perimeter(self) -> float:
        # You're own your own here
        return 0.0
