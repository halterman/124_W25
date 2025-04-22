# File rectangle.py

from point import Point
from shape import Shape


class Rectangle(Shape):
    def __init__(self, corner: Point, length: float, width: float) -> None:
        self.corner = corner
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2*self.length + 2*self.width

    def lengthen(self) -> None:
        self.length += 1

    def widen(self) -> None:
        self.width += 1