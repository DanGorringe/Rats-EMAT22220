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

# Main loop, only require as many steps as nodes
# as will clear a node each day

# can only go to t-2 days as looks forward

for t in range(len(nodeList)-2):
    # Choose node to attack
    attackNode = LookForward1(infectedList)

    # Update each of our lists
    clearedList.append(attackNode)
    infectedList.remove(attackNode)
    attackNode.ownership = blue
    # Draw the network and save it
    graph1.draw(1000,1000,'./test/'+format(t+1,'03d')+'.png')



# Then choose the node by the smallest change in defenders

attackNode = lowestDefenderChoice(infectedList)
clearedList.append(attackNode)
infectedList.remove(attackNode)
attackNode.ownership = blue
graph1.draw(1000,1000,'./test/'+format(len(nodeList)-1,'03d')+'.png')

# Now choose the last node

attackNode = infectedList[0]
clearedList.append(attackNode)
infectedList.remove(attackNode)
attackNode.ownership = blue
graph1.draw(1000,1000,'./test/'+format(len(nodeList),'03d')+'.png')
