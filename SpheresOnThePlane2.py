import maya.cmds as mc
import random

class SpheresOnThePlane():
	def __init__(self, size = 10.0, maxRadius = 1, numSpheres = 15):
		self.size = size
		self.spherePlane = mc.polyPlane(axis = [0,1,0], height = self.size, width = self.size)
		self.numVertices = mc.polyEvaluate(self.spherePlane,  vertex = True)
		self.numSpheres = numSpheres
		self.sphereNames = []
		self.maxRadius = maxRadius
		vertices = random.sample(range(self.numVertices), self.numSpheres)
		for v in vertices:
			radius = random.uniform(1, self.maxRadius)
			position = mc.pointPosition(self.spherePlane[0]+".vtx["+str(v)+"]")
			self.sphereNames.append(mc.polySphere(r = radius)[0])
			mc.move(position[0], radius, position[2])

	def randomizeSpheres(self):
		vertices = random.sample(range(self.numVertices), self.numSpheres)
		index = 0
		for v in vertices:
			radius = random.uniform(1, self.maxRadius)
			position = mc.pointPosition(self.spherePlane[0]+".vtx["+str(v)+"]")
			mc.select(self.sphereNames[index])
			mc.move(position[0], radius, position[2])
			index += 1

	def changeNumber(self, newNumSpheres = 15):
		if newNumSpheres>self.numSpheres:
			vertices = random.sample(range(self.numVertices), newNumSpheres)
			for v in vertices:
				radius = random.uniform(1, self.maxRadius)
				position = mc.pointPosition(self.spherePlane[0]+".vtx["+str(v)+"]")
				self.sphereNames.append(mc.polySphere(r = radius)[0])
				mc.move(position[0], radius, position[2])

		if newNumSpheres<self.numSpheres:
			i = self.numSpheres - newNumSpheres
			while i>0:
				mc.delete(self.sphereNames[i])
				i -=1

		self.numSpheres = newNumSpheres

	def resizeGrid(self, newSize = 10):
		for sphere in self.sphereNames:
			mc.select(sphere, add = True)
		mc.select(self.spherePlane, add = True)
		selection = mc.ls(sl = True)
		tempGroup = mc.group(selection, name = "TempGroup")
		scaleFactor = newSize/ self.size
		mc.select(tempGroup)
		mc.scale(scaleFactor, scaleFactor, scaleFactor, r = True)
		self.size = newSize

spherePlane1 = SpheresOnThePlane()
spherePlane1.randomizeSpheres()

spherePlane2 = SpheresOnThePlane()
spherePlane2.changeNumber(26)

spherePlane3 = SpheresOnThePlane()
spherePlane3.resizeGrid(20)