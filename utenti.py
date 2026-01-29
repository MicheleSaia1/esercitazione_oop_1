from math import math


class Utente:
    tessera_id=1

    
    
    
    def __init__(self, nome,):
        self.nome= nome
        self.id = Utente.tessera_id
        Utente.contatore += 1
       

        
    def __repr__(self):
        return f"Utente=(nome={self.nome},id= :{self.id})"
        
        
    def __eq__(self, other):
        if not isinstance(self,other):
            return False
        
        else:
            return self.nome == other.nome
        
    

    


        
        