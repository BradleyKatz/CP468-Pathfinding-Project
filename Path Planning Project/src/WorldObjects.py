from graphics import Point, Rectangle

"""
Very simple classes that wrap around graphics.py's Rectangle class.
Essentially, these classes exist just for the sake of being able to call
our objects BlankTiles, Obstacles, Robots, and RendezvousPoints in our code
"""

class BlankTile(Rectangle):
    def __init__(self, x, y, scale, numRobots):
        super().__init__(Point(scale * x, scale * y), Point(scale * x + scale, scale * y + scale))
        self.xPos = x
        self.yPos = y
        self.parent = None
        
        # Make each node contain a list of costs to maintain the costs for each robot without copying the world a million times.
        self.costsFromStart = [None] * numRobots
        self.estCostToGoal = 0
        
        self.setFill("white")

class RendezvousPoint(Rectangle):
    def __init__(self, x, y, scale, numRobots):
        super().__init__(Point(scale * x, scale * y), Point(scale * x + scale, scale * y + scale))
        self.xPos = x
        self.yPos = y
        self.parent = None
        
        # Make each node contain a list of costs to maintain the costs for each robot without copying the world a million times.
        self.costsFromStart = [None] * numRobots
        self.estCostToGoal = 0
        
        self.setFill("blue")

class Robot(Rectangle):
    def __init__(self, x, y, scale, rid):
        super().__init__(Point(scale * x, scale * y), Point(scale * x + scale, scale * y + scale))
        self.x0 = 0
        self.y0 = 0
        self.xPos = x
        self.yPos = y
        self.scaleFactor = scale
        self.robotID = rid # Used to index costsFromStart
        self.atGoal = False
        
        # Since each robot searches separately, they should maintain their own open and closed lists
        self.frontier = []
        self.explored = []
        
        self.setFill("red")
    
class Obstacle(Rectangle):
    def __init__(self, x, y, scale, numRobots):
        super().__init__(Point(x * scale, y * scale), Point(scale * x + scale, scale * y + scale))
        self.xPos = x
        self.yPos = y
        self.parent = None
        
        # Make each node contain a list of costs to maintain the costs for each robot without copying the world a million times.
        self.costsFromStart = [None] * numRobots
        self.estCostToGoal = 0
        
        self.setFill("black")