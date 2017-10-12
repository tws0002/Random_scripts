import maya.cmds as mc

controlName = mc.ls(sl = True)[0]
groupName = mc.listRelatives(controlName, parent = True)
jointName = mc.ls(sl = True)[1]

mc.parent(groupName, jointName)
mc.makeIdentity(groupName, apply=True, t=1, r=1, s=1, n=0)
mc.parent(groupName, world = True)
mc.parentConstraint(controlName, jointName)