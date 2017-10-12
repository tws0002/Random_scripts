from PySide import QtGui
from PySide import QtCore
from PySide import QtSignal
from PySide import QtSlot

class testWidget(QtGui.QWidget):
	def __init__(self):

		self.threadWorker = testObject()
		self.thread = QtCore.QThread()
		self.threadWorker.moveToThread(self.thread)
		self.thread.start()

		testLayout = QtGui.QVBoxLayout()
		self.setLayout(testLayout)
		self.testButton = QtGui.QPushButton()
		self.threadButton.clicked.connect(self.threadWorker.test)
		testLayout.addWidget(self.testButton)
		

class testObject(QtCore.QObject):
	def __init__(self):
		pass

	def test(self, args*):
		print 'tested!'
		pass

def main():
	app = QtGui.QApplication(sys.argv)
	test = testWidget()
	test.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()