from graphics import *
from WorldObjects import BlankTile, RendezvousPoint, Robot, Obstacle

# constants
READ_ONLY = "r"
SPACE_BAR = "space"
SCALE_FACTOR = 50

# global variables
robots = []
worldTiles = []

roomHeight = 0
roomWidth = 0
numRobots = 0
rendezvousPoint = None

def init():
    validFileGiven = False

    # Prompt user for a filename until they enter a valid name / path of a txt file
    while not validFileGiven:
        filename = input("Enter the name of the room layout txt file: ")
        
        try:
            inputStream = open(filename, READ_ONLY, encoding="utf-8")
            validFileGiven = True
        except:
            print("ERROR: File Not Found")
    
    # Read in room layout and other problem information from the txt file
    currentLine = inputStream.readline().split()
    global roomHeight
    roomHeight = int(currentLine[0])
    global roomWidth 
    roomWidth = int(currentLine[1])
    
    # Read in number of robots to create
    global numRobots
    numRobots = int(inputStream.readline())
    
    # Read in the starting coordinates of each robot
    for i in range(0, numRobots):
        currentLine = inputStream.readline().split()
        robots.append(Robot(SCALE_FACTOR * int(currentLine[1]), SCALE_FACTOR * int(currentLine[0]), SCALE_FACTOR))
    
    # Read in the location of the rendezvous point    
    currentLine = inputStream.readline().split()
    global rendezvousPoint
    rendezvousPoint = RendezvousPoint(SCALE_FACTOR * int(currentLine[1]), SCALE_FACTOR * int(currentLine[0]), SCALE_FACTOR)
        
    
    # Read in the layout of the room points
    """
    Example of how points in the room work.
    0 denotes an empty tile
    1 denotes an obstacle tile
    
        0123456789
    
    0   1000000001
    1   1100000011
    2   0000000000
    3   1000110001
    4   1001111001
    5   0001111000
    6   0000110000
    7   1100000011
    """
    for i in range(0, roomHeight):
        currentLine = list(inputStream.readline()) 
        worldTiles.append([])
        
        for j in range(0, len(currentLine)):
            if currentLine[j] == "0":
                worldTiles[len(worldTiles) - 1].append(BlankTile(SCALE_FACTOR * j, SCALE_FACTOR * (len(worldTiles) - 1), SCALE_FACTOR))
            elif currentLine[j] == "1":
                worldTiles[len(worldTiles) - 1].append(Obstacle(SCALE_FACTOR * j, SCALE_FACTOR * (len(worldTiles) - 1), SCALE_FACTOR)) 
    
    inputStream.close()

def displayWorld(win):
    """
    Use this function to create draw every object at their initial positions.
    
    Displays everything in the room in the following order:
    - Floor tiles and obstacles
    - Robots
    - Rendezvous point
    """
    for row in worldTiles:
        for tile in row:
            tile.draw(win)
    
    for robot in robots:
        robot.draw(win)
        
    rendezvousPoint.draw(win)

# Parse txt file for problem information and initialize display window
init()
window = GraphWin("Path Planning Robots", roomWidth * SCALE_FACTOR, roomHeight * SCALE_FACTOR)

displayWorld(window)

while window.isOpen():
    try:
        if (window.getKey() == SPACE_BAR):
            # Placeholder: This block will be replaced with code to display a single step of the algorithm
            print("AWW YISS SPACE!")
    except:
        print("", end="") # Waste computation by being really freaking dumb