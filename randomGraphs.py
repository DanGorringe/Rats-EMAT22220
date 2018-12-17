# e-rat-ication

import graph as gp
import algorithms as al

import random
'''
blue = (0,0,255)
red = (255,0,0)
'''
blue = (102,221,170) # Medium aquamarine
red = (255,125,0)    # orange


'''
xMax = 4
yMax = 4

nodeList = []
edgeList = []

# Shit me it's difficult to fill 2d arrays with unique instances of objects
nodeMatrix = []
for j in range(yMax):
    nodeMatrix.append([gp.Node(ownership=red) for i in range(xMax)])

y = 0
for row in nodeMatrix:
    x = 0
    for node in row:
        # Just add coordiantes, so that we can draw a nice diagram
        node.coordinates = [200+200*x,200+200*y]
        # Adding edges randomly?
        options = []
        # to the left
        if x < xMax-1:
            options.append(nodeMatrix[y][x+1])
        # below
        if y < yMax-1:
            options.append(nodeMatrix[y+1][x])
            if x != 0:
                options.append(nodeMatrix[y+1][x-1])
        random.shuffle(options)
        if len(options) != 0:
            lim = random.randint(1,len(options))
            for k in range(lim):
                addingNode = options[-1]
                newEdge = gp.Edge(node,addingNode)
                edgeList.append(newEdge)
                options.pop()
        nodeList.append(node)
        x += 1
    y += 1

graph1 = gp.Graph(nodeList,edgeList)
graph1.draw(10000,10000,'test.png')
#al.LookForward1Method(graph1)
answerPrims = al.WeirdPrims(graph1,'./TestPrim/')
answerOther = al.LookForward1Method(graph1,'./TestOther/')
print(answerPrims)
print(answerOther)
'''


def RandoGraph(n):
    xMax = n
    yMax = n

    nodeList = []
    edgeList = []

    # Shit me it's difficult to fill 2d arrays with unique instances of objects
    nodeMatrix = []
    for j in range(yMax):
        nodeMatrix.append([gp.Node(ownership=red) for i in range(xMax)])

    y = 0
    for row in nodeMatrix:
        x = 0
        for node in row:
            # Adding edges randomly?
            options = []
            # to the left
            if x < xMax-1:
                options.append(nodeMatrix[y][x+1])
            # below
            if y < yMax-1:
                options.append(nodeMatrix[y+1][x])
                if x != 0:
                    options.append(nodeMatrix[y+1][x-1])
            random.shuffle(options)
            if len(options) != 0:
                lim = random.randint(1,len(options))
                for k in range(lim):
                    addingNode = options[-1]
                    newEdge = gp.Edge(node,addingNode)
                    edgeList.append(newEdge)
                    options.pop()
            nodeList.append(node)
            x += 1
        y += 1

    graph = gp.Graph(nodeList,edgeList)
    return(graph)

data = []

for n in range(2,15):
    for i in range(20):
        graph1 = RandoGraph(n)
        answerPrims = al.WeirdPrims(graph1)
        answerOther = al.LookForward1Method(graph1)
        answerKruskals = al.Kruskal(graph1)
        data.append([n*n,answerPrims,answerOther,answerKruskals])

import csv

myFile = open('data.csv', 'w')
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(data)
