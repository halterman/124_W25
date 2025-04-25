# File point.py

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
    

def distance(p1: Point, p2: Point) -> float:
    x1 = p1.x
    y1 = p1.y
    x2 = p2.x
    y2 = p2.y
    # Add your code from the Geometry assignment
    result = 0.0  # Replace with your code
    return result
