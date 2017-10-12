import sys
import math
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

nodeName = "RippleDeformer"
nodeId = OpenMaya.MTypeId(0x102fff)

class Ripple(OpenMayaMPx.MPxDeformerNode):
    '''
    Commands ----> MPxCommand
    Custom ------> MPxNode
    Deformer ----> MPxDeformerNode
    '''
    mObj_Amplitude = OpenMaya.MObject()
    mObj_Displace = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
    
    def deform(self, dataBlock, geoIterator, matrix, geometryIndex):
        input = OpenMayaMPx.cvar.MPxDeformerNode_input
        
        # 1: Attach a handle to input Array Attribute
        dataHandleInputArray = dataBlock.outputArrayValue(input)

        # 2. Jump to particular element 
        dataHandleInputArray.jumpToElement(geometryIndex)

        # 3. Attach the handle to specific data block
        dataHandleInputElement = dataHandleInputArray.outputValue()

        # 4. Reach to the child

        outputGeom = OpenMayaMPx.cvar.MPxGeometryFilter_outputGeom
        dataHandleInputGeom = dataHandleInputElement.child(inputGeom)
        inMesh = dataHandleInputGeom.asMesh()

        envelope = OpenMayaMPx.cvar.MPxDeformerNode_envelope
        dataHandleEnveloppe = dataBlock.inputValue(envelope)
        envelopeValue = dataHandleEnveloppe.asFloat()

        dataHandleAmplitude = dataBlock.inputValue(Ripple.mObj_Amplitude)
        amplitudeValue = dataHandleAmplitude.asFloat()

        dataHandleDisplace = dataBlock.inputValue(Ripple.mObj_Displace)
        displaceValue = dataHandleDisplace.asFloat()

        mFloatVectorArray_normal = OpenMaya.MFloatVectorArray()
        mFnMesh = OpenMaya.MFnMesh(inMesh)
        mFnMesh.getVertexNormals(False, mFloatVectorArray_normal, OpenMaya.MSpace.kObject)

        mPointArray_meshVert = OpenMaya.MPointArray()
        while(not geoIterator.isDone()):
            pointPosition = geoIterator.position()
            weight = self.weightValue(dataBlock, geometryIndex, geoIterator.index())
            pointPosition.x = pointPosition.x + math.sin( geoIterator.index() + displaceValue) * amplitudeValue * mFloatVectorArray_normal[geoIterator.index()].x * weight* envelopeValue
            pointPosition.y = pointPosition.y + math.sin( geoIterator.index() + displaceValue) * amplitudeValue * mFloatVectorArray_normal[geoIterator.index()].y * weight* envelopeValue
            pointPosition.z = pointPosition.z + math.sin( geoIterator.index() + displaceValue) * amplitudeValue * mFloatVectorArray_normal[geoIterator.index()].z * weight*envelopeValue
            # geoIterator.setPosition(pointPosition)
            mPointArray_meshVert.append(pointPosition)
            geoIterator.next()

        geoIterator.setAllPositions(mPointArray_meshVert)
        
    
def deformerCreate():
    nodePtr = OpenMayaMPx.asMPxPtr(Ripple())
    return nodePtr

def nodeInitializer():
    '''
    Create Attributes
    Attach Attributes
    Design Circuitry
    '''
    mFnAttr = OpenMaya.MFnNumericAttribute()
    Ripple.mObj_Amplitude = mFnAttr.create("Attribute Value", "AttrVal", OpenMaya.MFnNumericData.kFloat, 0.0)

    mFnAttr.setKeyable(1)
    mFnAttr.setMin(0.0)
    mFnAttr.setMax(1.0)

    Ripple.mObj_Displace = mFnAttr.create("DisplaceValue", "DispVal", OpenMaya.MFnNumericData.kFloat, 0.0)
    mFnAttr.setKeyable(1)
    mFnAttr.setMin(0.0)
    mFnAttr.setMax(10.0)

    Ripple.addAttribute(Ripple.mObj_Amplitude)
    Ripple.addAttribute(Ripple.mObj_Displace)

    '''
    SWIG = Simplified Wrapper Interface Generator
    '''

    outputGeom = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    Ripple.attributeAffects(Ripple.mObj_Amplitude, outputGeom)
    Ripple.attributeAffects(Ripple.mObj_Displace, outputGeom)
    
def initializePlugin(mObject):
    mPlugin = OpenMayaMPx.MFnPlugin(mObject, "Shobhit Khinvasara", "1.0")
    try:
        mPlugin.registerNode(nodeName, nodeId, deformerCreate, nodeInitializer, OpenMayaMPx.MPxNode.kDeformerNode)
        
    except:
        sys.stderr.write("Failed to register node: %s" % nodeName)
        raise

def uninitializePlugin(mObject):
    mPlugin = OpenMayaMPx.MFnPlugin(mObject)
    try:
        mPlugin.deregisterNode(nodeId)
    except:
        sys.stderr.write("Failed to deregister node: %s " % nodeName)
        raise


