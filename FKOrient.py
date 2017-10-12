import maya.cmds as cmds

def FKOrient():
	selectedObjects = cmds.ls(selection =  True)
	if len(selectedObjects) != 2:
		print "Wrong number of objects selected"
		return
		
	cmds.parent(selectedObjects[0], selectedObjects[1], relative = True)
	cmds.makeIdentity(selectedObjects[0], apply = True)
	cmds.parent(selectedObjects[0], world = True, relative = True)
	
FKOrient()