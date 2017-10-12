import maya.cmds as cmds

#first select the control, then  the joint to be controlled
def FKControl():
	selectedObjects = cmds.ls(selection =  True)
	if len(selectedObjects) != 2:
		print "Wrong number of objects selected"
		return
		
	parentOfControl = cmds.listRelatives(selectedObjects[0], parent = True)
	print parentOfControl
	print selectedObjects[0]
	cmds.parent(parentOfControl, selectedObjects[1], relative = True)
	cmds.makeIdentity(parentOfControl)
	cmds.parent(parentOfControl, world = True)
	parentOfJoint = cmds.listRelatives(selectedObjects[1], parent = True)
	print parentOfJoint
	print selectedObjects[1]
	#cmds.parent(selectedObjects[1], world = True)
	cmds.parent(selectedObjects[1], selectedObjects[0], relative = True)
	#cmds.parent(parentOfControl, parentOfJoint, relative = True)
	print "Success"
	
FKControl()