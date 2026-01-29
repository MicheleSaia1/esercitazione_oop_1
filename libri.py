class Libri:


     def __init__(self, autore="",nazionalita="",titolo="",isbn="" ):
           
           self.autore= autore
           self.nazionalita=nazionalita
           self.titolo= titolo
           self.isbn=isbn
           
           
        
       

        
     def __repr__ (self): 
      return f"classe libri, (titolo:{self.titolo}, autore : {self.autore}, nazionalità dell'autore : {self.nazionalita}, codice isbn :{self.isbn} ) "
        
        
     def __eq__ (self, other):
      if not isinstance(self,other):
        return False
        
      return self.autore == other.autore, self.nazionalita==other.nazionalita ,self.titolo == other.titolo and self.isbn==other.isbn 
       

     def descrizione (self):
        print(self.titolo,self.autore, self.nazionalita, self.isbn)

        


    