from PyQt4 import QtGui
from PyQt4.QtCore import QObject, pyqtSlot
from Carta import Carta


class GUI_Carta(QtGui.QPushButton, Carta):
	def __init__(self):
		QtGui.QPushButton.__init__(self)
		self.setFixedWidth(50)
		Carta.__init__(self,"A")

	@pyqtSlot()		
	def onclick(self):
		print "cliccato"
		self.setStyleSheet("background-image: url(prova.png);")
		return 0
