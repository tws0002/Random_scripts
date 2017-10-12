import maya.cmds as mc

objects = mc.ls(sl = True)

objLocList = {}

for obj in objects:
    objLoc = mc.xform(obj, worldSpace = True, query = True, translation = True)
    objLocList[obj] = objLoc

index = 0
for obj in objLocList:
	mc.move(0, 5+i, 0, objLocList[obj])

selectedObject = mc.ls(sl = True)

if selectedObject in objLocList:
	objOldLoc = objLocList[selectedObject]
	mc.move(objOldLoc[0], objOldLoc[1], objOldLoc[2], selectedObject)