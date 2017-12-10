
class Carta:
	COPERTA  =0
	SCOPERTA =1
	FUORI    =2

	def __init__(self, c ):
		self.valore=c
		self.stato=self.COPERTA
		
	def get_valore(self ):
		return self.valore 
	
	def is_fuori( self ):
		return ( self.stato == self.FUORI )
	
	def is_scoperta(self):
		return ( self.stato == self.SCOPERTA )
	
	def viene_tolta_dal_tavolo(self):
		self.stato = self.FUORI	

	def viene_scoperta(self):
		self.stato = self.SCOPERTA 
	
	def viene_coperta(self):
		self.stato = self.COPERTA 
		
	def is_coperta(self):
		return ( self.stato == self.COPERTA )
		
	def is_uguale_a ( self , c ):
		return ( self.valore == c.get_valore() ) 
