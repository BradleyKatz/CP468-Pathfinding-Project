from graphics import *
from WorldObjects import BlankTile, RendezvousPoint, Robot, Obstacle
from search import initGoalCosts, computeNextStep
from math import fabs
import time

# constants
READ_ONLY = "r"
SPACE_BAR = "space"
ENTER_KEY = "Return"
SCALE_FACTOR = 50
TIME_DELAY = 0.5

# global variables
robots = []
worldTiles = []

roomHeight = 0
roomWidth = 0
numRobots = 0
rendezvousPoint = None

autopilotMode = False

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
        robots.append(Robot(int(currentLine[0]), int(currentLine[1]), SCALE_FACTOR, i))
    
    # Read in the location of the rendezvous point    
    currentLine = inputStream.readline().split()
    global rendezvousPoint
    rendezvousPoint = RendezvousPoint(int(currentLine[0]), int(currentLine[1]), SCALE_FACTOR, numRobots)
        
    
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
                worldTiles[len(worldTiles) - 1].append(BlankTile(j, (len(worldTiles) - 1), SCALE_FACTOR, numRobots))
            elif currentLine[j] == "1":
                worldTiles[len(worldTiles) - 1].append(Obstacle(j, (len(worldTiles) - 1), SCALE_FACTOR, numRobots)) 
            
    inputStream.close()
    initGoalCosts(worldTiles, rendezvousPoint)
    
    for robot in robots:
        worldTiles[robot.yPos][robot.xPos].costsFromStart[robot.robotID] = 0
        robot.frontier.append(worldTiles[robot.yPos][robot.xPos])

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
solvedCompletely = False

while window.isOpen() and not solvedCompletely:
    key = window.checkKey()
    numSolved = 0
    
    if key == ENTER_KEY:
        autopilotMode = not autopilotMode
    
    if autopilotMode or key == SPACE_BAR:
        for robot in robots:
            if not robot.atGoal:
                computeNextStep(robot, rendezvousPoint, worldTiles)
                robot.move((robot.xPos - robot.x0) * SCALE_FACTOR, (robot.yPos - robot.y0) * SCALE_FACTOR)
            
            print("Robot {} --- X: {}          Y:{}".format(robot.robotID, robot.xPos, robot.yPos))
            
            if robot.atGoal:
                numSolved += 1
        
        print()
        
        if autopilotMode:
            time.sleep(TIME_DELAY)
    if numSolved == numRobots:
        solvedCompletely = True
        
for robot in robots:
    robot.move((robot.xPos - robot.x0) * SCALE_FACTOR, (robot.yPos - robot.y0) * SCALE_FACTOR)

print("PRESS ANY KEY TO EXIT")
window.getKey()
sys.exit(1)