
'''
blue = (0,0,255)
red = (255,0,0)
'''

blue = (102,221,170) # Medium aquamarine
red = (255,125,0)    # orange

# Return the node with the smallest change in defenders
def lowestDefenderChoice(nodeList):
    # Initial best value as just the total number of nodes
    currentBest = len(nodeList)
    # Just set current best as the first
    currentBestNode = nodeList[0]
    for node in nodeList:
        defendersRequired = node.attractivness()
        if defendersRequired < currentBest:
            currentBestNode = node
            currentBest = defendersRequired
    return currentBestNode

# Returns the node which allows the smallest change in defenders after looking ahead one timestep
def LookForward1(nodeListInput):
    currentBest = len(nodeListInput)
    currentBestNode = nodeListInput[0]
    currentDefenders = len(nodeListInput)

    for node in nodeListInput:
        # Pretend this node has been added
        iterableList = list(nodeListInput)
        iterableList.remove(node)
        nodeDefenders = node.attractivness()
        # Temporarily change ownership
        node.ownership = blue
        nodeBestNode = lowestDefenderChoice(iterableList)
        nodeBest = nodeDefenders + nodeBestNode.attractivness()
        node.ownership = red
        if nodeBest <= currentBest:
            if nodeDefenders < currentDefenders:
                currentDefenders = nodeDefenders
                currentBestNode = node
                currentBest = nodeBest
    return(currentBestNode)



##############
# FunkyPrims #
##############

# Uses our prims-like algorithm to clear the input graph
# Will save a picture of the graph at every stage
# Also prints the totalDefenders days used

def WeirdPrims(graph,outputPath=None):

    if outputPath != None:
        graph.draw(1000,1000,outputPath+format(0,'03d')+'.png')

    # two simple lists to keep track
    infectedList = list(graph.nodeList)
    clearedList = []

    totalDefenders = 0

    # Algo: choose the node with hgihesst attractivness in the cleared list

    attackNode = lowestDefenderChoice(infectedList)
    attackNode.ownership = blue
    clearedList.append(attackNode)
    infectedList.remove(attackNode)
    if outputPath != None:
        graph.draw(1000,1000,outputPath+format(1,'03d')+'.png')

    # Check the number of defneders
    totalDefenders += graph.defendersCheck(blue)

    # Options are the nodes that are directly connected to those eradicated
    options = attackNode.connections



    for t in range(len(graph.nodeList)-1):
        attackNode = lowestDefenderChoice(options)

        # Update each of our lists
        clearedList.append(attackNode)
        infectedList.remove(attackNode)

        # Remove the node chosen from the options
        # extend by all the new options from attacked node
        # Remove all those options which have already been taken
        options.remove(attackNode)
        options.extend(attackNode.connections)
        options = [x for x in options if x not in clearedList]

        attackNode.ownership = blue
        # Draw the network and save it
        if outputPath != None:
            graph.draw(1000,1000,outputPath+format(t+2,'03d')+'.png')

        # Check the number of defneders
        totalDefenders += graph.defendersCheck(blue)
    return(totalDefenders)

################
# Look-forward #
################

def LookForward1Method(graph,outputPath=None):

    for node in graph.nodeList:
        node.ownership = red

    if outputPath != None:
        graph.draw(1000,1000,outputPath+format(0,'03d')+'.png')

    # two simple lists to keep track
    infectedList = list(graph.nodeList)
    clearedList = []

    totalDefenders = 0

    # Main loop, only require as many steps as nodes
    # as will clear a node each day

    # can only go to t-2 days as looks forward

    for t in range(len(graph.nodeList)-2):
        # Choose node to attack
        attackNode = LookForward1(infectedList)
        # Update each of our lists
        clearedList.append(attackNode)
        infectedList.remove(attackNode)
        attackNode.ownership = blue

        totalDefenders += graph.defendersCheck(blue)

        # Draw the network and save it

        if outputPath != None:
            graph.draw(1000,1000,outputPath+format(t+1,'03d')+'.png')



    # Then choose the node by the smallest change in defenders

    attackNode = lowestDefenderChoice(infectedList)
    clearedList.append(attackNode)
    infectedList.remove(attackNode)
    attackNode.ownership = blue

    if outputPath != None:
        graph.draw(1000,1000,outputPath+format(len(graph.nodeList)-1,'03d')+'.png')

    totalDefenders += graph.defendersCheck(blue)

    # Now choose the last node
    attackNode = infectedList[0]
    clearedList.append(attackNode)
    infectedList.remove(attackNode)
    attackNode.ownership = blue

    if outputPath != None:
        graph.draw(1000,1000,outputPath+format(len(graph.nodeList),'03d')+'.png')


    totalDefenders += graph.defendersCheck(blue)

    return(totalDefenders)

#############
# Kruskal's #
#############

def Kruskal(graph,outputPath=None):

    for node in graph.nodeList:
        node.ownership = red

    if outputPath != None:
        graph.draw(1000,1000,outputPath+format(0,'03d')+'.png')

    # two simple lists to keep track
    infectedList = list(graph.nodeList)
    clearedList = []

    totalDefenders = 0

    # Main loop, only require as many steps as nodes
    # as will clear a node each day

    # can only go to t-2 days as looks forward

    for t in range(len(graph.nodeList)):
        # Choose node to attack
        attackNode = lowestDefenderChoice(infectedList)
        # Update each of our lists
        clearedList.append(attackNode)
        infectedList.remove(attackNode)
        attackNode.ownership = blue

        totalDefenders += graph.defendersCheck(blue)

        # Draw the network and save it

        if outputPath != None:
            graph.draw(1000,1000,outputPath+format(t+1,'03d')+'.png')

    return(totalDefenders)
