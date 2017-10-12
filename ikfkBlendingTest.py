import maya.cmds as mc
from maya import OpenMaya

def createFKControl():
	joint1= mc.ls(sl = True)[0]
	joint2 = mc.listRelatives(joint1, children = True)[0]
	joint3 = mc.listRelatives(joint2, children = True)[0]
	FKControls = []
	FKControlGroups = []
	for joint in [joint1, joint2, joint3]:
		controlObject = mc.circle( nr=(1, 0, 0), c=(0, 0, 0), r = 1)[0]
		controlName = joint.rpartition("_")[0] + "_CTL"
		FKControlObject = mc.rename(controlObject, controlName)
		FKControls.append(FKControlObject)
		mc.setAttr(FKControlObject+'.translateX', mc.xform(joint, query = True, worldSpace = True, translation = True)[0])
		mc.setAttr(FKControlObject+'.translateY', mc.xform(joint, query = True, worldSpace = True, translation = True)[1])
		mc.setAttr(FKControlObject+'.translateZ', mc.xform(joint, query = True, worldSpace = True, translation = True)[2])
		FKControlObjectShape = mc.listRelatives(FKControlObject, children = True)
		mc.setAttr(FKControlObjectShape[0]+".overrideEnabled", 1)
		mc.setAttr(FKControlObjectShape[0]+".overrideColor", 13)
		groupName = mc.group(FKControlObject, n = joint.rpartition("_")[0] + "_GRP")   
		mc.parent(groupName, joint)
		mc.makeIdentity(groupName, apply=True, t=1, r=1, s=1, n=0)
		mc.parent(groupName, world = True)
		controlParent = mc.listRelatives(FKControlObject, parent = True)[0]
		mc.parentConstraint(FKControlObject, joint)
		FKControlGroups.append(groupName)
		#if controlParent != None:
			#mc.parent(groupTrueName, FKControlObject)
	mc.parent(FKControlGroups[2], FKControls[1])
	mc.parent(FKControlGroups[1], FKControls[0])
			
createFKControl()

def createIKControl():

	#Find the position of poleVectorControl
	joint1 = mc.ls(sl = True)[0]
	joint2 = mc.listRelatives(joint1, children = True)[0]
	joint3 = mc.listRelatives(joint2, children = True)[0]

	joint1Pos = mc.xform(joint1, q = True, ws = True, t = True)
	joint2Pos = mc.xform(joint2, q = True, ws = True, t = True)
	joint3Pos = mc.xform(joint3, q = True, ws = True, t = True)

	startV = OpenMaya.MVector(joint1Pos[0] ,joint1Pos[1],joint1Pos[2])
	midV = OpenMaya.MVector(joint2Pos[0] ,joint2Pos[1],joint2Pos[2])
	endV = OpenMaya.MVector(joint3Pos[0] ,joint3Pos[1],joint3Pos[2])

	startEnd = endV - startV
	startMid = midV - startV

	dotP = startMid * startEnd

	proj = float(dotP) / float(startEnd.length())

	startEndN = startEnd.normal()

	projV = startEndN * proj

	arrowV = startMid - projV

	arrowV*= 0.5 
 
	finalV = arrowV + midV

	loc = mc.spaceLocator()[0]

	mc.xform(loc , ws =1 , t= (finalV.x , finalV.y ,finalV.z))

	ikHandle = mc.ikHandle(sj = joint1, ee = joint3, sol = "ikRPsolver")

	poleVector = mc.poleVectorConstraint(loc, ikHandle)

def blending():
	blendColorNode1 = mc.shadingNode("blendColor", n = joint1)


import maya.cmds as mc

circle1 = mc.listRelatives(mc.circle( nr=(1, 0, 0), c=(0, 0, 0), r = 1)[0], children = True)[0]
circle2 = mc.listRelatives(mc.circle( nr=(0, 1, 0), c=(0, 0, 0), r = 1)[0], children = True)[0]
circle3 = mc.listRelatives(mc.circle( nr=(0, 0, 1), c=(0, 0, 0), r = 1)[0], children = True)[0]
groupName = mc.group(empty = True, n = "ikControl")
mc.parent(circle1, groupName, relative = True, shape = True)
mc.parent(circle2, groupName, relative = True, shape = True)
mc.parent(circle3, groupName, relative = True, shape = True)
