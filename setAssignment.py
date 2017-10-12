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
		
		self.selectionLayout = qg.QHBoxLayout()
		self.layout().addLayout(self.selectionLayout)

		selectionButton_layout = qg.QHBoxLayout()
		select_1stSetButton = qg.QPushButton('Select First Group')
		select_2ndSetButton = qg.QPushButton('Select Second Group')
		selectionButton_layout.addWidget(select_1stSetButton)
		selectionButton_layout.addWidget(select_2ndSetButton)

		self.layout().addLayout(selectionButton_layout)

		select_1stSetButton.clicked.connect(self.select_1stSet)
		select_2ndSetButton.clicked.connect(self.select_2ndSet)

		self.stacked_layout = qg.QStackedLayout()
		self.layout().addLayout(self.stacked_layout)

		self.selectionLayout = qg.QHBoxLayout()
		self.layout().addLayout(self.selectionLayout)

		setSelectionButton_layout = qg.QVBoxLayout()
		unionButton = qg.QPushButton('Union')
		intersectionButton = qg.QPushButton('Intersection')
		diff_12_Button = qg.QPushButton('Difference between 1st and 2nd set')
		diff_21_Button = qg.QPushButton('Difference between 2nd and 1st set')
		setSelectionButton_layout.addWidget(unionButton)
		setSelectionButton_layout.addWidget(intersectionButton)
		setSelectionButton_layout.addWidget(diff_12_Button)
		setSelectionButton_layout.addWidget(diff_21_Button)

		unionButton.clicked.connect(self.selectUnion)
		intersectionButton.clicked.connect(self.selectIntersection)
		diff_12_Button.clicked.connect(self.select_12_Diff)
		diff_21_Button.clicked.connect(self.select_21_Diff)


		self.layout().addLayout(setSelectionButton_layout)

	def select_1stSet(self):
		self.groupSet1 = set(mc.ls(selection = True))

	def select_2ndSet(self):
		self.groupSet2 = set(mc.ls(selection = True))

	def selectUnion(self):
		mc.select(clear = True)
		for obj in self.groupSet1.union(self.groupSet2):
			mc.select(obj, add = True)

	def selectIntersection(self):
		mc.select(clear = True)
		for obj in self.groupSet1.intersection(self.groupSet2):
			mc.select(obj, add = True)

	def select_12_Diff(self):
		mc.select(clear = True)
		for obj in self.groupSet1.difference(self.groupSet2):
			mc.select(obj, add = True)

	def select_21_Diff(self):
		mc.select(clear = True)
		for obj in self.groupSet2.difference(self.groupSet1):
			mc.select(obj, add = True)


dialog = SetUI()
dialog.show()