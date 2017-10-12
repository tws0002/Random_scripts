import maya.cmds as mc

control = mc.ls(sl = True)[0]
controlName = control.rpartition("_")[0]
groupName = mc.group(control, n = controlName + "_GRP") 