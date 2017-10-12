import maya.cmds as mc
import pymel.core as pm

vertex = mc.ls(sl = True)[0]
control = mc.ls(sl = True)[1]
clusterHandle = mc.ls(sl = True)[2]
controlParent = mc.listRelatives(control, parent = True)[0]

mc.parent(control, world = True)
mc.select(vertex, controlParent)
pm.runtime.PointOnPolyConstraint()

#break rotate connections and set them 0

mc.parent(control, controlParent)
mc.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
mc.connectAttr(control+".translate", clusterHandle+".translate")
mc.connectAttr(control+".rotate", clusterHandle+".rotate")
negOffsetGRP = mc.group(control, name = control.rpartition("_")[0]+"_negOffset_GRP")
negativeOffset = mc.shadingNode("multiplyDivide", asUtility = True)
mc.setAttr(negativeOffset+".input2X", -1)
mc.setAttr(negativeOffset+".input2Y", -1)
mc.setAttr(negativeOffset+".input2Z", -1)
mc.connectAttr(control+".translate",negativeOffset+".input1")
mc.connectAttr(negativeOffset+".output", negOffsetGRP+".translate")