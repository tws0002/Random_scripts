import maya.cmds as cmds

def FKParent():
	selectedObjects = cmds.ls(selection =  True)
	if len(selectedObjects) != 2:
		print "Wrong number of objects selected"
		return
		
	cmds.parent(selectedObjects[0], selectedObjects[1], relative = True)
	cmds.makeIdentity(selectedObjects[0])
	cmds.parent(selectedObjects[0], world = True)
	shapeOfSelectedObject = cmds.listRelatives(selectedObjects[0], shapes = True)
	cmds.parent(shapeOfSelectedObject, selectedObjects[1], relative = True, shape = True)
	print "Success"
	
FKParent()