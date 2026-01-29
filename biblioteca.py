class Biblioteca:
    
    
    
     def __init__(self,utente,libri, ):
           self.utente=utente
           self.libri=libri
           self.disponibilita= True
        
       

        
     def __repr__(self):
           return f"classe biblioteca: utente: {self.utente} , libri : {self.libri} , disponibilità: {self.disponibilità}"
        
            
            
     def __eq__(self, other):
             if not isinstance(self,other):
              return False
             
             return self.utente == other.utente, self.libri == other.libri, self.disponibilita == other.disponibilita
    
        
            

    