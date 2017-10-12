
#######
# Create center locator in center of eye and call it 'center'
#  Select top then bottom verts then run:

import maya.cmds as mc
from maya import cmds , OpenMaya


center= 'L_eyeCenter_LOC'

vtx = mc.ls(sl=1, fl=1)

for v in vtx:
    mc.select(cl=1)
    jnt = mc.joint(n='lid'+v+'')
    pos = mc.xform ( v, q=1, ws=1, t=1)
    mc.xform(jnt, ws=1, t=pos)
    posC= mc.xform(center, q=1, ws=1, t=1)
    mc.select(cl=1)
    jntC=mc.joint()
    mc.xform (jntC, ws=1, t=posC)
    mc.parent(jnt, jntC)

    #orient joints
    mc.joint (jntC, e=1, oj='xyz', secondaryAxisOrient='yup', ch=1, zso=1)


##Group and rename each


#### Aim locator setup:
## Create up vector from Center and call it 'L_eyeUpVec_LOC'
##Select joint tips and run: (same for both top and bottom)
sel = mc.ls (sl=1)
for s in sel:
	loc =mc.spaceLocator(n = s.rpartition("_")[0]+"_LOC")[0]
	pos =mc.xform(s, q=1, ws=1, t=1)
	mc.xform(loc, ws=1, t=pos)
	par=mc.listRelatives(s, p=1,)[0]
	mc.aimConstraint(loc, par, mo=1, weight=1, aimVector= (1,0,0), upVector = (0,1,0), worldUpType='object', worldUpObject='L_eyeUpVec_LOC' )

#Group locators together and rename


####################################################
###### Curve create section:

#### RUN THIS FIRST ######
def getUParam( pnt = [], crv = None):

    point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
    curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
    paramUtill=OpenMaya.MScriptUtil()
    paramPtr=paramUtill.asDoublePtr()
    isOnCurve = curveFn.isPointOnCurve(point)
    if isOnCurve == True:
        
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    else :
        point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    
    param = paramUtill.getDouble(paramPtr)  
    return param

def getDagPath( objectName):
    
    if isinstance(objectName, list)==True:
        oNodeList=[]
        for o in objectName:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(o)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            oNodeList.append(oNode)
        return oNodeList
    else:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(objectName)
        oNode = OpenMaya.MDagPath()
        selectionList.getDagPath(0, oNode)
        return oNode

########

####create LINEAR curve with one point PER locator (both top and bottom)


##select locators then run:
sel=mc.ls(sl=1)
#Shapename of curve VVVV
crv= 'uplidCurveShape'

for s in sel:
	pos=mc.xform(s, q=1, ws=1, t=1)
	u = getUParam(pos, crv)
	#create point on curve node. Make sure Locators have suffix of _LOX
	name= s.replace('_LOC', '_PCI')
	pci= mc.createNode('pointOnCurveInfo', n=name)
	mc.connectAttr(crv+'.worldSpace', pci+'.inputCurve')
	mc.setAttr(pci+'.parameter', u)
	mc.connectAttr(pci+'.position', s+'.t')

##### rename curve to high for high density.



#Next Create lo resolution curve to drive the higher res Curve
# Create 5 point curve using cubic. Corners, 1 middle and 2 supportive.

#After Creating curve manually fit the curve to match the higher resolution curve.
#rename it to low


#Select the high then the lower and then create a Wire deformer


# Create circle controls for main an secondary controls
# have a zero group inserted.
# position controls at the same postion as the low res cv's.
# Name controls appropriately and give them color
# group them together.

#Add an 0-1 integer attribute to main top and bottom controls called 'secondaryCnt' 
# connect this new attribute to the secondary controls visiblity


#create joints for each secondary and main control
#name joints appropriately

#Skin low resolution curve to joints created. 


#Point constraint joints to controls.

#Create parent constraint group for secondary controls that is point constrainted between
# main top/bottom controls and the corners. 


##########################################################
# Create smart blink setup:

# Duplicate the lo res uplid curve and name it blink_Crv

# Select the (lower res) uplid curve, lolid curve and finally the new blink curve and create blendshape.

# Add a 0-1 interger attribute on the main uplid control called smartBlinkHeight 

#Connect the smartblinkheight attribute to the blendshape and then reverse for the other curve shape.


# duplicate both upper and lower high resolution curves and rename them blink


#set the blink height to the highest position
#Then create a wire deformer between the High resolution blink curve and the blink height as the driver.
# set the scale attribute in the wire deformer to be 0

# do the same for the lower lid curve 

# change the order of operation for the curve to  have the wire under the blendshape.



##Add 0-1 interger attribute on both upper and lower main lid controls called 'smartBlink'
# Hook atribute to blensshape thank blinks the curves.

# weight eye and complete.