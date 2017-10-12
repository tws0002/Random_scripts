import PySide.QTCore as qc
import PySide.QTGui as qg

dialog = None

class NameIt(qg.QDialog):
	def __init__(self):
		qg.QDialog.__init__(self)
		self.setWindowFlags(qc.qt.WindowStaysOnTopHint)
		self.setWindowTitle("Name it")
		self.setFixedHeight(285)
		self.setFixedWidth(320)

		self.setLayout(qg.QVBoxLayout())
		self.layout().setContentMargins(5,5,5,5)
		self.layout().setSpacing(0)
		self.layout().setAlignment(qc.Qt.AlignTop)
