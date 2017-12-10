from TEXT_Partita import Partita

print "ciao"



while True :
	
	p =Partita()
	
	p.gioca()
	
	risposta  = raw_input(" vuoi giocare ancora ( Y/N )?" )
	
	if risposta =="n":
		break

print "goobye dal main"
	
