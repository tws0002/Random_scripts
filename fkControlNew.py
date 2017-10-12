import maya.cmds as mc

def createFKControl():
	jointNames = mc.ls(sl = True)
	for j in jointNames:
		controlObject = mc.circle( nr=(0, 0, 1), c=(0, 0, 0), r = 2)[0]
		controlName = j.rpartition("_")[0] + "_CTL"
		FKControlObject = mc.rename(controlObject, controlName)
		mc.setAttr(FKControlObject+'.translateX', mc.xform(j, query = True, worldSpace = True, translation = True)[0])
		mc.setAttr(FKControlObject+'.translateY', mc.xform(j, query = True, worldSpace = True, translation = True)[1])
		mc.setAttr(FKControlObject+'.translateZ', mc.xform(j, query = True, worldSpace = True, translation = True)[2])
		FKControlObjectShape = mc.listRelatives(FKControlObject, children = True)
		mc.setAttr(FKControlObjectShape[0]+".overrideEnabled", 1)
		mc.setAttr(FKControlObjectShape[0]+".overrideColor", 17)
		groupName = mc.group(FKControlObject, n = j.rpartition("_")[0] + "_GRP")
		mc.parent(groupName, j)
		mc.makeIdentity(groupName, apply=True, t=1, r=1, s=1, n=0)
		mc.parent(groupName, world = True)
		jointParent = mc.listRelatives(j, parent = True)
		mc.parentConstraint(FKControlObject, j)
		if jointParent != None:
			mc.parent(groupName, jointParent)

createFKControl()