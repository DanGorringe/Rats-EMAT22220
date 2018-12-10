# Only needed for graph drawing
from PIL import ImageFont, ImageDraw, Image

class Node():

    def __init__(self,coordinates=None,ownership=None,radius=20):
        # The Co-ordinates of the node
        self.coordinates = coordinates
        # Ownership, as the form of the RGB tuple of colour
        self.ownership = ownership
        self.radius = radius
        self.connections = []

    def draw(self,draw):
        coordinates = self.coordinates
        circleRadius = self.radius
        circleBox = [coordinates[0]-circleRadius,coordinates[1]-circleRadius,coordinates[0]+circleRadius,coordinates[1]+circleRadius]
        draw.ellipse(circleBox,self.ownership)

    def connectionAppend(self,A):
        self.connections.append(A)

    def diffOwnConnections(self):
        # Returns a list of all the differently owned connections of this node
        diffOwnList = []
        for node in self.connections:
            if node.ownership != self.ownership:
                diffOwnList.append(node)
        return diffOwnList

    def attractivness(self):
        # Using the formulae: infected - defended
        # returns the change in defenders caused by choosing this node
        infectedConnected = len(self.diffOwnConnections())
        defendedConnected = len(self.connections) - infectedConnected
        return(infectedConnected-defendedConnected)



class Edge():

    def __init__(self,A,B,lineWidth=5):
        #self.connection = [A,B].sort()
        self.connection = [A,B]
        self.lineWidth = lineWidth
        A.connectionAppend(B)
        B.connectionAppend(A)

    def draw(self,draw):
        [A,B] = self.connection
        midpoint = [(A.coordinates[0]+B.coordinates[0])/2,(A.coordinates[1]+B.coordinates[1])/2]
        # Draw line from A to midpoint
        draw.line((A.coordinates[0],A.coordinates[1],midpoint[0],midpoint[1]),A.ownership,width=self.lineWidth)
        # Draw line from A to midpoint
        draw.line((B.coordinates[0],B.coordinates[1],midpoint[0],midpoint[1]),B.ownership,width=self.lineWidth)


class Graph():

    def __init__(self,nodeList,edgeList):
        self.nodeList = nodeList
        self.edgeList = edgeList

    def draw(self,maxXCoord,maxYCoord,fileString):
        # Open blank image
        image = Image.new("RGB", (maxXCoord, maxYCoord), (255,255,255))
        # Alternativly, Instead open a png to draw over
        #image = Image.open("iow.png")
        draw = ImageDraw.Draw(image)

        for edge in self.edgeList:
            edge.draw(draw)

        for node in self.nodeList:
            node.draw(draw)

        # Save as the given fileString
        image.save(fileString)
