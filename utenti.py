


class Utente:   
    
    
    def __init__(self, nome,id, max_libri,registrati):
        self.nome= nome
        self.id=id
        registrati=[]
        self.max_libri=[0]*3



        
    def __repr__(self):
        return f"Utente=(nome={self.nome},id= :{self.id})"
        
        
    def __eq__(self, other):
        if not isinstance(self,other):
            return False
        
        
        return self.nome == other.nome ,self.id == other.id , self.registrati == other.registrati and self.max_libri == other.max_libri
    
    
    def iscrizione(self, registrati):
        if registrati in self.registrati:
            print("l'utente è già registrato")
            return False
        
        if registrati.aggiungi_utente(self):
            self.registrati.append(registrati)
            return True

        
        



        
        
    

    


        
        