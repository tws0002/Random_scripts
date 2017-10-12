import maya.cmds as cmds
def offsetGroup():
	selectedObject = cmds.ls(selection = True)
	print selectedObject
	if len(selectedObject) > 1:
		print "Wrong number of objects selected"
		return
	else:
		for obj in selectedObject:
			cmds.group(obj, n =obj[0])
	
offsetGroup()