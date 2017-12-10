import os
from Carta import Carta




class Partita:
	
	def __init__(self ):
		
		self.numero_carte_sul_tavolo=10
		
		self.mazzo_di_carte=[Carta('A') , Carta('B') , Carta('C'),
						Carta('D') , Carta('E') , Carta('A'),
						Carta('B') , Carta('C') , Carta('D'),
						Carta('E')]
						
		self.stampa_le_carte_sul_tavolo()
	
	def gioca (self):
		print "ho giocato"
		
	def stampa_le_carte_sul_tavolo(self):
		
		os.system('cls||clear')
		
		for i in range(0,10):
			if self.mazzo_di_carte[i].is_fuori():
				print "    ",
			else: print i,"  ",
		
		print

		for i in range(0,10):
			if self.mazzo_di_carte[i].is_fuori() :
				print "    ",
			elif self.mazzo_di_carte[i].is_coperta() :
				print "X   ", 
			else: print self.mazzo_di_carte[i].get_valore(),"  ",
			
		print 
			
	
	def una_carta_scelta_e_scoperta_dallo_utente(self, messaggio):
		
		while True :
			i = input("scegli " + messaggio + " carta ")
			
			if self.mazzo_di_carte[i].is_coperta() :
				break
				
		self.mazzo_di_carte[i].viene_scoperta()
		self.stampa_le_carte_sul_tavolo()
		return self.mazzo_di_carte[i]
	
	def gioca(self) :

		while True :
			carta1 = self.una_carta_scelta_e_scoperta_dallo_utente("una")
			carta2 = self.una_carta_scelta_e_scoperta_dallo_utente("un'altra")
					
			if carta1.is_uguale_a(carta2) :
				
				carta1.viene_tolta_dal_tavolo()
				carta2.viene_tolta_dal_tavolo()
				
				self.numero_carte_sul_tavolo = self.numero_carte_sul_tavolo - 2 ;
				
				if self.numero_carte_sul_tavolo == 0 :
					break
			else :
				carta1.viene_coperta()
				carta2.viene_coperta()

