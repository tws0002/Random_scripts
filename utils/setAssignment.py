import PySide.QtCore as qc
import PySide.QtGui as qg

import maya.cmds as mc

class SetUI(qg.QDialog):
	def __init__(self):
		qg.QDialog.__init__(self)
		self.setWindowTitle("Set Selection")
		self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
		self.setModal(False)
		self.setFixedHeight(250)
		self.setFixedWidth(250)
		
		self.setLayout(qg.QVBoxLayout())
		self.stacked_layout = qg.QStackedLayout()
		self.layout().addLayout(self.stacked_layout)

		setSelectionButton_layout = qg.QVBoxLayout()
		unionButton = qg.QPushButton('Select Union')
		intersectionButton = qg.QPushButton('Select Intersection')
		differenceButton = qg.QPushButton('Select Difference')

		setSelectionButton_layout.addWidget(unionButton)
		setSelectionButton_layout.addWidget(intersectionButton)
		setSelectionButton_layout.addWidget(differenceButton)

		self.layout().addLayout(setSelectionButton_layout)

dialog = SetUI()
dialog.show()