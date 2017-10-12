import maya.cmds as mc
import random

class vertexList():
    plane = ''
    def __init__(self, number=10):
        if not vertexList.plane:
            vertexList.plane = cmds.polyPlane( sx=10, sy=10, w=10, h=10)[0]

        numVertices = cmds.polyEvaluate( vertexList.plane, vertex = True )
        self.vertices =  random.sample( range(numVertices), 10 )
        self.positions = []        
        for vertex in self.vertices:
            position = cmds.pointPosition( vertexList.plane + '.vtx[' + str(vertex) + ']' )
            self.positions.append(position)
            cmds.polyMoveVertex( vertexList.plane + ".vtx[" + str(vertex) + "]", translateY=2 )
        
    def vertexRevert(self):
        for i, vertex in enumerate(self.vertices):
            print vertex
            print self.positions[i]
            cmds.polyMoveVertex( vertexList.plane + ".vtx[" + str(vertex) + "]", \
            translateY= -2, ws=True)
    def __add__(self, other):
        combination = vertexList(0)
        combination.vertices = self.vertices + other.vertices
        combination.positions = self.positions + other.positions
        
        return combination
    def __str__(self):
        stringList = [str(vertex) for vertex in self.vertices]
        return self.plane + " with vertices " + " ,".join(stringList )
        
class planeDeformation():
	def __init__(self):
		vertexList = []
		vertextList.append(vertexList())

myplane = planeDeformation()
