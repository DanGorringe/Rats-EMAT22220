

blue = (0,0,255)
red = (255,0,0)

# Return the node with the smallest change in defenders
def lowestDefenderChoice(nodeList):
    # Initial best value as just the total number of nodes
    currentBest = -len(nodeList)
    # Just set current best as the first
    currentBestNode = nodeList[0]
    for node in nodeList:
        defendersRequired = node.attractivness()
        if defendersRequired > currentBest:
            currentBestNode = node
            currentBest = defendersRequired
    return currentBestNode

# Returns the node which allows the smallest change in defenders after looking ahead one timestep
def LookForward1(nodeListInput):
    currentBest = len(nodeListInput)
    currentBestNode = nodeListInput[0]
    for node in nodeListInput:
        # Pretend this node has been added
        iterableList = list(nodeListInput)
        iterableList.remove(node)
        # Temporarily change ownership
        node.ownership = blue
        nodeBestNode = lowestDefenderChoice(iterableList)
        nodeBest = node.attractivness() + nodeBestNode.attractivness()
        node.ownership = red
        if nodeBest < currentBest:
            currentBestNode = node
            currentBest = nodeBest
    return(currentBestNode)


##############
# FunkyPrims #
##############

# Uses our prims-like algorithm to clear the input graph
# Will save a picture of the graoh at every stage
# Also prints the totalDefenders days used

def WeirdPrims(graph):

    graph.draw(1000,1000,'./test/'+format(0,'03d')+'.png')

    # two simple lists to keep track
    infectedList = list(graph.nodeList)
    clearedList = []

    totalDefenders = 0

    # Algo: choose the node with hgihesst attractivness in the cleared list

    attackNode = lowestDefenderChoice(infectedList)
    attackNode.ownership = blue
    clearedList.append(attackNode)
    infectedList.remove(attackNode)
    graph.draw(1000,1000,'./test/'+format(1,'03d')+'.png')

    # Check the number of defneders
    totalDefenders += graph.defendersCheck(blue)
    print(totalDefenders)

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
        graph.draw(1000,1000,'./test/'+format(t+2,'03d')+'.png')

        # Check the number of defneders
        totalDefenders += graph.defendersCheck(blue)
        print(totalDefenders)

################
# Look-forward #
################

def LookForward1Method(graph):

    graph.draw(1000,1000,'./test/'+format(0,'03d')+'.png')

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
        print(totalDefenders)

        # Draw the network and save it
        graph.draw(1000,1000,'./test/'+format(t+1,'03d')+'.png')



    # Then choose the node by the smallest change in defenders

    attackNode = lowestDefenderChoice(infectedList)
    clearedList.append(attackNode)
    infectedList.remove(attackNode)
    attackNode.ownership = blue
    graph.draw(1000,1000,'./test/'+format(len(graph.nodeList)-1,'03d')+'.png')

    totalDefenders += graph.defendersCheck(blue)

    # Now choose the last node
    attackNode = infectedList[0]
    clearedList.append(attackNode)
    infectedList.remove(attackNode)
    attackNode.ownership = blue
    graph.draw(1000,1000,'./test/'+format(len(graph.nodeList),'03d')+'.png')


    totalDefenders += graph.defendersCheck(blue)

    print(totalDefenders)
