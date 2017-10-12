import PySide.QtCore as qc
import PySide.QtGui as qg

import maya.cmds as mc
import pymel.core as pm
from utils.generic import undo_pm
from functools import partial

START = 'start'
END = 'end'
CACHE = 'cache'
NODE = 'node'


class InterpolateIt(qg.QDialog):
	def __init__(self):
		qg.QDialog.__init__(self)
		self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
		self.setWindowTitle('Interpolate It')

		self.setLayout(qg.QVBoxLayout())
		self.layout().setContentsMargins(5,5,5,5)
		self.layout().setSpacing(5)

		selectLayout = qg.QHBoxLayout()
		buttonLayout = qg.QHBoxLayout()
		sliderLayout = qg.QHBoxLayout()
		checkLayout  = qg.QHBoxLayout()

		self.layout().addLayout(selectLayout)
		self.layout().addLayout(buttonLayout)
		self.layout().addLayout(sliderLayout)
		self.layout().addLayout(checkLayout)

		storeItems = qg.QPushButton('Store Items')
		clearItems = qg.QPushButton('Clear Items')

		selectLayout.addSpacerItem(qg.QSpacerItem(5,5,qg.QSizePolicy.Expanding))
		selectLayout.addWidget(storeItems)
		selectLayout.addWidget(clearItems)
		selectLayout.addSpacerItem(qg.QSpacerItem(5,5,qg.QSizePolicy.Expanding))

		self.storeStartButton = qg.QPushButton('Store Start')
		self.resetItemButton = qg.QPushButton('Reset')
		self.storeEndButton = qg.QPushButton('Store End')

		buttonLayout.addWidget(self.storeStartButton)
		buttonLayout.addWidget(self.resetItemButton)
		buttonLayout.addWidget(self.storeEndButton)

		self.startLabel = qg.QLabel('Start')
		self.slider = qg.QSlider()
		self.slider.setRange(0, 49)
		self.slider.setOrientation(qc.Qt.Horizontal)
		self.endLabel = qg.QLabel('End')

		sliderLayout.addWidget(self.startLabel)
		sliderLayout.addWidget(self.slider)
		sliderLayout.addWidget(self.endLabel)

		self.transformsCheckBox = qg.QCheckBox('Transform')
		self.attributesCheckBox = qg.QCheckBox('UD Attrbutes')
		self.transformsCheckBox.setCheckState(qc.Qt.Checked )
		checkLayout.addWidget(self.transformsCheckBox)
		checkLayout.addWidget(self.attributesCheckBox)

		self.items = {}

		storeItems.clicked.connect(self.storeItems)
		clearItems.clicked.connect(self.clearItems)

		self.storeStartButton.clicked.connect(self.storeStart)
		self.storeEndButton.clicked.connect(self.storeEnd)

		self.slider.valueChanged.connect(self.setLinearInterpolation)
		self.slider.sliderReleased.connect(self._endSliderUndo)

		self.enableButtons(False)

	def _startSliderUndo(self):


	def storeItems(self):
		selection = pm.ls(sl = True, fl = True)
		if not selection:
			return

		self.items = {}
		for node in selection:
			self.items[node.name()] = {NODE:node, START:{}, END :{}, CACHE : {}  }

		self.enableButtons(True)

	def clearItems(self):
		self.items = {}
		self.enableButtons(False)

	def enableButtons(self, value):
		self.storeStartButton.setEnabled(value)
		self.resetItemButton.setEnabled(value)
		self.storeEndButton.setEnabled(value)
		self.transformsCheckBox.setEnabled(value)
		self.attributesCheckBox.setEnabled(value)
		self.slider.setEnabled(value)
		self.startLabel.setEnabled(value)
		self.endLabel.setEnabled(value)

	def storeStart(self):
		if not self.items: return
		self._store(START, 0)

	def storeEnd(self):
		if not self.items: return
		self._store(END, 50)

	def _store(self, key, value):
		for item_dict in self.items.values():
			node = item_dict[NODE]
			attrs = self.getAttributes(node)
			data = item_dict[key]
			for attr in attrs:
				data[attr] = node.attr(attr).get()

			print item_dict

		self.slider.blockSignals(True)
		self.slider.setValue(value)
		self.slider.blockSignals(False)

	def _cache(self):
		for item_dict in self.items.values():
			node = item_dict[NODE]

			start = item_dict[START]
			end = item_dict[END]

			if not start or not end:
				item_dict[CACHE] = None
				continue

			attrs = list(set(start.keys()) and set(end.keys()))

			cache = item_dict[CACHE] = {}
			for attr in attrs:
				startAttr = start[attr]
				endAttr = end[attr]

				if startAttr == endAttr:
					cache[attr] = None

				else:
					cacheValues = cache[attr] = []
					interval = float(endAttr - startAttr)/49.0
					 for index in range(50):
                        cacheValues.append((interval * index) + startAttr)


	def getAttributes(self, node):
		attrs = []
		if self.transformsCheckBox.isChecked():
			for transform in 'trs':
				for axis in 'xyz':
					channel = '%s%s' %(transform, axis)
					if node.attr(channel).isLocked(): continue
					attrs.append(channel)

		return attrs

	def resetAttributes(self, *args):
		if not self.items:
			return

		for item_dict in self.items.values():
			node  = item_dict[NODE]
			attrs = self.getAttributes(node)

			for attr in attrs:
				defaultValue = pm.attributeQuery(attr, node = node, ld = True)[0]
				node.attr(attr).set(defaultValue)

	def setLinearInterpolation(self, value):
		if not self.items: return

		for item_dict in self.items.values():
			node = item_dict[NODE]
			start = item_dict[START]

			if not start or not item_dict[END]: continue

			for attr in cache.keys():
				if cache[attr] == None: continue
				node.attr(attr).set(cache[attr][value])

dialog = None

def create():
	global dialog
	if dialog is None:
		dialog = InterpolateIt()

	dialog.show()

def delete():
	global dialog
	if dialog is None:
		return

	dialog.deleteLater()
	dialog = None

stuff = create()


