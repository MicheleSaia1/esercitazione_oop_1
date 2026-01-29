class Libri:


     def __init__(self, autore="",nazionalità="",titolo="",isbn="" ):
           
           self.autore= autore
           self.nazionalita=
           self.titolo= titolo
           self.isbn=isbn
        
       

        
    def __repr__ (self): 
     return f"classe libri, (titolo:{self.titolo}, autore : {self.autore}, nazionalità dell'autore : {self.nazionalità}, codice isbn :{self.isbn} ) "
        
        
    def __eq__(self, other):
     if not isinstance(self,other):
        return False
        
     return self.autore == other.autore, self.nazionalita==other.nazionalità,self.titolo == other.titolo and self.isbn==other.isbn 
       
        