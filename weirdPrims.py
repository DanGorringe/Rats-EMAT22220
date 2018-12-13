# e-rat-ication

import graph as gp
import csv

blue = (0,0,255)
red = (255,0,0)

# The csv file to load is a bit weird
# think that you can only mention connections once
# otherwise weird stuff might happen for the number of connections

nodeList = []
csvEdgeList = []

with open('./csvFiles/list.csv','r') as csvfile1:
    csv = csv.reader(csvfile1,delimiter=',')
    i = 0
    for line in csv:
        # Lines are in format: x,y,e,..
        # - e's are index numbers for nodes connected with
        # e.g.  a,b,2
        #       c,d
        # Means that there is an edge between (a,b) and (c,d)
        nodeCoords = (line[0],line[1])
        nodeCoords = list(map(int,nodeCoords))
        nodeList.append(gp.Node(nodeCoords,red))
        connections = line[2:]
        for b in connections:
            csvEdgeList.append([i,int(b)])
        i = i+1

edgeList = []

for edge in csvEdgeList:
    A = nodeList[edge[0]]
    B = nodeList[edge[1]]
    edge2Add = gp.Edge(A,B)
    edgeList.append(edge2Add)

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
    currentBestNode = nodeList[0]
    for node in nodeListInput:
        # Pretend this node has been added
        iterableList = list(nodeListInput)
        iterableList.remove(node)
        # Temporarily change ownership
        node.ownership = blue
        nodeBestNode = lowestDefenderChoice(iterableList)
        node.ownership = red
        nodeBest = node.attractivness() + nodeBestNode.attractivness()
        if nodeBest < currentBest:
            currentBestNode = node
            currentBest = nodeBest
    return(currentBestNode)



##################
# Graph clearing #
##################

graph1 = gp.Graph(nodeList,edgeList)
graph1.draw(1000,1000,'./test/'+format(0,'03d')+'.png')

# two simple lists to keep track
infectedList = list(nodeList)
clearedList = []

# Algo: choose the node with hgihesst attractivness in the cleared list

attackNode = lowestDefenderChoice(infectedList)
attackNode.ownership = blue
clearedList.append(attackNode)
infectedList.remove(attackNode)
graph1.draw(1000,1000,'./test/'+format(1,'03d')+'.png')

# Options are the nodes that are directly connected to those eradicated
options = attackNode.connections



for t in range(len(nodeList)-1):
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
    graph1.draw(1000,1000,'./test/'+format(t+2,'03d')+'.png')
