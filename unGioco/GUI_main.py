
import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari
from PyQt4.QtCore import QObject,pyqtSlot
from PyQt4.QtGui import QGridLayout, QWidget,QPushButton


from GUI_Carta import GUI_Carta


class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self) 
		self.resize(350, 250) # ridimensiona la finestra
		self.setWindowTitle('MainWindow')
		# self.statusBar().showMessage('Messaggio') # crea una veloce barra di stato
	
class GUI_Partita( QtGui.QWidget ) :
	def __init__(self, window ) :
		QWidget.__init__(self)
		
		grid = QGridLayout( self )
		c=0
		for valore in ["A","B","C","D","E","A","B","C","D","E"] :
			
			gc = GUI_Carta(valore)
			self.connect( gc, QtCore.SIGNAL('clicked()'), QtCore.SLOT('onCartaCliccata()'))
			
			grid.addWidget( gc, c / 5  , c%5)
			c=c+1
		window.setCentralWidget ( self )
	
		self.carte_scoperte=0
		self.numero_carte_sul_tavolo=10
		
		
	@pyqtSlot()		
	def onCartaCliccata(self):
		carta_cliccata = self.sender()
		
		print self.sender().get_valore()
		
		if carta_cliccata.is_fuori() :
			return
		if carta_cliccata.is_scoperta():
			return
		
		carta_cliccata.viene_scoperta();
		if  self.carte_scoperte == 0 :
			
			self.prima_carta = carta_cliccata
			self.carte_scoperte = 1
			
		elif self.carte_scoperte == 1 :
		
			if carta_cliccata.is_uguale_a ( self.prima_carta ):
				self.prima_carta.viene_tolta_dal_tavolo()
				carta_cliccata.viene_tolta_dal_tavolo()
				self.carte_scoperte=0
			else :
				self.seconda_carta = carta_cliccata
				self.carte_scoperte = 2 
		
		elif self.carte_scoperte == 2 :
			self.prima_carta.viene_coperta()
			self.seconda_carta.viene_coperta()
			
			self.prima_carta = carta_cliccata
			self.carte_scoperte = 1
			
			
	
		
		


app = QtGui.QApplication(sys.argv)

main = MainWindow()

partita = GUI_Partita( main )


main.show()

sys.exit(app.exec_())
