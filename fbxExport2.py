#The real process for FBX export:
#1: Set Project.
#2: Create Reference of the rig
#3: Do the animation and save the file
#4: Import the reference(Go to reference editor, select the reference file, right-click=>File=>Import Objects from reference)
#5: Select Joints
#6: Bake Animation
#7: Delete Constraints, controls and mesh 
#8: Unparent Joints from their group and delete the group
#9: Export all as FBX in the same location as the rig reference file
#10: Open the reference file.

import maya.cmds as mc

filePath = mc.file(query = True, l = True)[0]
fileDirectory = filePath.rpartition("/")[0]
fileNumber = int((filePath.rpartition("_")[2]).rpartition(".")[0])
mc.file(rename = fileDirectory+"/mayaAnimation_"+str(fileNumber + 1)+".ma")
mc.file( f = True, save = True, type = "mayaAscii")
mc.file(fileDirectory+"/baseRig_1.ma", importReference = True)
mc.bakeResults ("baseRig_1:*_JNT", simulation=True, t=(1, 48), sampleBy=1 ,disableImplicitControl=True, preserveOutsideKeys=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)
mc.delete("baseRig_1:*Constraint*")
mc.delete("baseRig_1:*_CTL")
mc.delete("baseRig_1:*_GEO")
mc.select("baseRig_1:*_JNT")
mc.file(rename = fileDirectory+"/mayaAnimation_"+str(fileNumber)+".ma")
mc.file(fileDirectory+"/Animation_"+str(fileNumber)+".fbx", force = True, options = "groups=1;ptgroups=1;materials=1;smoothing=1;normals=1", type="FBX export", pr = True, es = True)


