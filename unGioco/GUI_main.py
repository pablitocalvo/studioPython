
import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari
from PyQt4.QtCore import QObject, pyqtSlot


from Carta import Carta


class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self) 
		# self.resize(350, 250) # ridimensiona la finestra
		self.setWindowTitle('MainWindow')
		# self.statusBar().showMessage('Messaggio') # crea una veloce barra di stato
	
	@pyqtSlot()
	def cartaCliccata (self):
		print "cliccataaa"
		
class GUI_Carta(QtGui.QPushButton, Carta):
	def __init__(self):
		QtGui.QPushButton.__init__(self)
		Carta.__init__(self,"A")

	@pyqtSlot()		
	def onclick(self):
		print "cliccato"
		self.setStyleSheet("background-image: url(prova.png);")
		return 0

app = QtGui.QApplication(sys.argv)

main = MainWindow()

gcarta=GUI_Carta()

gcarta.connect(gcarta, QtCore.SIGNAL('clicked()'), QtCore.SLOT('onclick()'));

main.setCentralWidget(gcarta)

main.show()

sys.exit(app.exec_())
