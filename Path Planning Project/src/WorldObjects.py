from graphics import Point, Rectangle

"""
Very simple classes that wrap around graphics.py's Rectangle class.
Essentially, these classes exist just for the sake of being able to call
our objects BlankTiles, Obstacles, Robots, and RendezvousPoints in our code
"""

class BlankTile(Rectangle):
    def __init__(self, x, y, scale):
        super().__init__(Point(x, y), Point(x + scale, y + scale))
        self.setFill("white")

class RendezvousPoint(Rectangle):
    def __init__(self, x, y, scale):
        super().__init__(Point(x, y), Point(x + scale, y + scale))
        self.setFill("blue")

class Robot(Rectangle):
    def __init__(self, x, y, scale):
        super().__init__(Point(x, y), Point(x + scale, y + scale))
        self.setFill("red")
    
class Obstacle(Rectangle):
    def __init__(self, x, y, scale):
        super().__init__(Point(x, y), Point(x + scale, y + scale))
        self.setFill("black")