# e-rat-ication

import graph as gp
import algorithms as al

import csv


blue = (0,0,255)
red = (255,0,0)

# The csv file to load is a bit weird
# think that you can only mention connections once
# otherwise weird stuff might happen for the number of connections

nodeList = []
csvEdgeList = []

with open('./csvFiles/list1.csv','r') as csvfile1:
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

graph1 = gp.Graph(nodeList,edgeList)
al.LookForward1Method(graph1)
