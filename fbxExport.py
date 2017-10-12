import maya.cmds as mc

filePath = mc.file(query = True, l = True)[0]
fileDirectory = filePath.rpartition("/")[0]
fileNumber = int((filePath.rpartition("_")[2]).rpartition(".")[0]) + 1
print filePath
print fileDirectory
print fileNumber
mc.bakeResults ("*_JNT", simulation=True, t=(1, 48), sampleBy=1 ,disableImplicitControl=True, preserveOutsideKeys=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)
mc.delete("*Constraint*")
mc.delete("*_CTL")
mc.select("*_JNT")
mc.select("*_GEO", add = True)
mc.file(fileDirectory+"/Animation_"+str(fileNumber)+".fbx", force = True, options = "groups=1;ptgroups=1;materials=1;smoothing=1;normals=1", type="FBX export", pr = True, es = True)
mc.file(rename = fileDirectory+"/mayaAnimation_"+str(fileNumber)+".ma")
mc.file( f = True, save = True, type = "mayaAscii")
mc.delete("*")
mc.file(fileDirectory+"/baseRig_1.ma", i = True, type="mayaAscii", ignoreVersion = True, mergeNamespacesOnClash = False, rpr = "baseFile", options="v=0;", pr = True)