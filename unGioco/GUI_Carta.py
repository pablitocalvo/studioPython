from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,QObject

from Carta import Carta


class GUI_Carta(QtGui.QPushButton, Carta):
	
	def __init__(self,  valore ):
		
		Carta.__init__(self,valore)
				
		QtGui.QPushButton.__init__(self)
		self.setFixedWidth(50)
		self.setFixedHeight(50)
		
		self.setStyleSheet("background: url(img/dorso.png); ")
		
	def viene_scoperta(self):
		Carta.viene_scoperta(self) 
		self.setStyleSheet("background: url(img/"+self.get_valore()+".png); ")

	def viene_coperta(self):
		Carta.viene_coperta(self)
		self.setStyleSheet("background: url(img/dorso.png); ")
		
	def viene_tolta_dal_tavolo(self):
		Carta.viene_tolta_dal_tavolo(self)
		self.setStyleSheet("background: url(img/none.png); ")
		
