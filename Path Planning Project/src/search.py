from WorldObjects import *
from math import fabs

def initGoalCosts(tiles, goal):
    for row in tiles:
        for tile in row:
            tile.estCostToGoal = fabs(tile.xPos - goal.xPos) + fabs(tile.yPos - goal.yPos)
        
def __addToFrontier__(robot, goal, nodeToAdd):
    if type(nodeToAdd) == Obstacle:
        # nodeToAdd is not a walkable tile, ignore it
        return
    
    if nodeToAdd.xPos == goal.xPos and nodeToAdd.yPos == goal.yPos:
        robot.x0 = robot.xPos
        robot.y0 = robot.yPos
        robot.xPos = goal.xPos
        robot.yPos = goal.yPos
        robot.atGoal = True
        return
    
    for node in robot.frontier:
        if node.xPos == nodeToAdd.xPos and node.yPos == nodeToAdd.yPos:
            # nodeToAdd is not more promising than a node that's already in the frontier, skip it
            return
            
    for node in robot.explored:
        if node.xPos == nodeToAdd.xPos and node.yPos == nodeToAdd.yPos:
            # We've already explored a more promising node than nodeToAdd, skip it
            return
            
    # If this part of the function is reached, nodeToAdd is promising and gets pushed onto the frontier
    robot.frontier.append(nodeToAdd)
        
# A* algorithm goes here!
def computeNextStep(robot, goal, tiles):
    # If the frontier is empty, we've reached the goal
    if len(robot.frontier) == 0 or robot.atGoal:
        return
        
    leastCostNode = robot.frontier[0]
    index = 0 
            
    # Pop least cost node from frontier
    for i in range(len(robot.frontier)):
        if type(robot.frontier[i]) == BlankTile and (robot.frontier[i].costsFromStart[robot.robotID] + robot.frontier[i].estCostToGoal) < (leastCostNode.costsFromStart[robot.robotID] + leastCostNode.estCostToGoal):
            index = i
            leastCostNode = robot.frontier[index]
            
    leastCostNode = robot.frontier.pop(index)
    
    # Update robot position variables to use later for redrawing in main
    robot.x0 = robot.xPos
    robot.y0 = robot.yPos
    robot.xPos = leastCostNode.xPos
    robot.yPos = leastCostNode.yPos
    
    # Generate successors of the least cost node and append them to the list
    if (leastCostNode.xPos > 0 and leastCostNode.xPos < len(tiles[0]) - 1):
        if (leastCostNode.yPos > 0 and leastCostNode.yPos < len(tiles) - 1):
            # There's a node to the left, right, up, and down
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos - 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos - 1])
            
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos + 1]) == BlankTile:    
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos + 1])
            
            if type(tiles[leastCostNode.yPos - 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos - 1][leastCostNode.xPos])
             
            if type(tiles[leastCostNode.yPos + 1][leastCostNode.xPos]) == BlankTile:   
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos + 1][leastCostNode.xPos])
        elif leastCostNode.yPos == 0:
            # There's a node to the left, right, and down
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos - 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos - 1])
            
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos + 1]) == BlankTile:    
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos + 1])
            
            if type(tiles[leastCostNode.yPos + 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos + 1][leastCostNode.xPos])
        elif leastCostNode.yPos == len(tiles) - 1:
            # There's a node to the left, right, and up
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos - 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos - 1])
            
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos + 1]) == BlankTile:    
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos + 1])
            
            if type(tiles[leastCostNode.yPos - 1][leastCostNode.xPos]) == BlankTile:   
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos - 1][leastCostNode.xPos])
    elif leastCostNode.xPos == 0:
        if leastCostNode.yPos == 0:
            # There's a node to the right and down
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos + 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos + 1])
            
            if type(tiles[leastCostNode.yPos + 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos + 1][leastCostNode.xPos])
        elif leastCostNode.yPos == len(tiles) - 1:
            # There's a node to the right and up
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos + 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos + 1])
            
            if type(tiles[leastCostNode.yPos - 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos - 1][leastCostNode.xPos])
        else:
            # There's a node to the right, up, and down
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos + 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos + 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos + 1])
            
            if type(tiles[leastCostNode.yPos - 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos - 1][leastCostNode.xPos])
            
            if type(tiles[leastCostNode.yPos + 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos + 1][leastCostNode.xPos])
    elif leastCostNode.xPos == len(tiles[0]) - 1:
        if leastCostNode.yPos == 0:
            # There's a node to the left and down
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos - 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos - 1])
            
            if type(tiles[leastCostNode.yPos + 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos + 1][leastCostNode.xPos])
        elif leastCostNode.yPos == len(tiles) - 1:
            # There's a node to the left and up
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos - 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos - 1])
            
            if type(tiles[leastCostNode.yPos - 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos - 1][leastCostNode.xPos])
        else:
            # There's a node to the left, up, and down
            if type(tiles[leastCostNode.yPos][leastCostNode.xPos - 1]) == BlankTile:
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].parent = leastCostNode
                tiles[leastCostNode.yPos][leastCostNode.xPos - 1].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos][leastCostNode.xPos - 1])
            
            if type(tiles[leastCostNode.yPos - 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos - 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos - 1][leastCostNode.xPos])
            
            if type(tiles[leastCostNode.yPos + 1][leastCostNode.xPos]) == BlankTile:
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].parent = leastCostNode
                tiles[leastCostNode.yPos + 1][leastCostNode.xPos].costsFromStart[robot.robotID] = leastCostNode.costsFromStart[robot.robotID] + 1
                __addToFrontier__(robot, goal, tiles[leastCostNode.yPos + 1][leastCostNode.xPos])
        
    robot.explored.append(leastCostNode)