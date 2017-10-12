import maya.cmds as mc
import random

class funnyPlane():
    plane = ""
    def __init__(self, numberOfVertices = 10):
        if not funnyPlane.plane:
            funnyPlane.plane = mc.polyPlane(sx = 10, sy = 10, w = 10, h = 10)[0]
        numVertices = mc.polyEvaluate(funnyPlane.plane, vertex = True)
        self.vertexList = []
        self.positions = []
        if numberOfVertices < numVertices:
            self.vertexList = random.sample(range(numVertices), numberOfVertices)
            for vertex in self.vertexList:
                position = mc.pointPosition(funnyPlane.plane+".vtx["+str(vertex)+"]")
                self.positions.append(position)
                mc.polyMoveVertex(funnyPlane.plane+".vtx["+str(vertex)+"]", translateY = 2)
                
    def vertexMove(self, min, max):
        for vertex in self.vertexList:
            position = random.uniform(min, max)
            mc.polyMoveVertex(funnyPlane.plane+".vtx["+str(vertex)+"]", translateY = position)

    def vertexRevert(self):
        for i, vertex in enumerate(self.vertexList):
            print "stuff"
            mc.polyMoveVertex(funnyPlane.plane+".vtx["+str(vertex)+"]", translateY = self.positions[i][1], ws = True)

    def __add__(self, other):
        combination = funnyPlane(0)
        combination.vertexList = self.vertexList+other.vertexList
        combination.positions = self.positions+other.positions
        return combination

    def __str__(self):
        return funnyPlane.plane+ " || ".join([str(vertex) for vertext in self.vertexList])

list1 = funnyPlane(10)
list2 = funnyPlane(20)
list3 = funnyPlane(10)

list2.vertexRevert()

list2.vertexMove(-1, 1)

newList = list1+list2

print newList