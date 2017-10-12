import PySide.QtCore as qc
import PySide.QtGui as qg
import maya.cmds as mc

import re

class CopySkinCluster(qg.QDialog):
	def __init__(self):
		qg.QDialog.__init__(self)
		self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
		self.setWindowTitle("Chassis Modeling")

		self.setLayout(qg.QVBoxLayout())
		self.layout().setContentsMargins(5,5,5,5)
		self.layout().setSpacing(5)

		sourcePrefixLayout = qg.QHBoxLayout()
		self.layout.addLayout(sourcePrefixLayout)

		sourcePrefixLabel = qg.QLabel("Source Prefix")
		sourcePrefixLayout.addWidget(sourcePrefixLabel)

		self.sourcePrefix = qg.QLineEdit()
		sourcePrefixLayout.addWidget(self.sourcePrefix)

		targetPrefixLayout = qg.QHBoxLayout()
		self.layout.addLayout(targetPrefixLayout)

		targetPrefixLabel = qg.QLabel("Source Prefix")
		targetPrefixLayout.addWidget(targetPrefixLabel)

		self.targetPrefix = qg.QLineEdit()
		targetPrefixLayout.addWidget(self.targetPrefix)

		self.copyButton = qg.QPushButton("Copy")
		self.copyButton.clicked.connect(self.copySkinCluster)
		self.layout.addWidget(self.copyButton)

		self.cancelButton - qg.QPushButton("Cancel")
		self.cancelButton.clicked.connect(self.cancel)
		self.layout.addWidget(self.cancelButton)

	def copySkinCluster(self):
		sourceSkin = mc.ls(sl = True)[0]
		targetSkin = mc.ls(sl = True)[1]

		sourcePrefix = self.sourcePrefix.text()
		targetPrefix = self.targetPrefix.text()

		for con in mc.listConnections(mc.listRelatives(sourceSkin, children = True)[0]):
			if mc.nodeType(con) == "skinCluster":
				sourceSkinCluster = con

		for con in mc.listConnections(mc.listRelatives(targetSkin, children = True)[0]):
			if mc.nodeType(con) == "skinCluster":
				targetSkinCluster = con

		sourceSkinClusterJoints = []
		for con in mc.listConnections(sourceSkinCluster, source = True ):
			if mc.nodeType(con.rpartition(".")[0]) == "joint":
				sourceSkinClusterJoints.append(con)

		targetSkinClusterJoints = []
		for con in mc.listConnections(targetSkinCluster, source = True):
			if mc.nodeType(con.rpartition(".")[0]) == "joint":
				targetSkinClusterJoints.append(con)

		if len(sourceSkinClusterJoints) != len(targetSkinClusterJoints):
			print "Number of joints not equal, Error!"
			return

		







