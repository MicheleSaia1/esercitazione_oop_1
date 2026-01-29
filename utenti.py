


class Utente:   
    
    
    def __init__(self, nome,id, max_libri):
        self.nome= nome
        self.id=id
        self.max_libri=[0]*3


        
    def __repr__(self):
        return f"Utente=(nome={self.nome},id= :{self.id})"
        
        
    def __eq__(self, other):
        if not isinstance(self,other):
            return False
        
        
        return self.nome == other.nome ,self.id == other.id and self.max_libri == other.max_libri
        
        
        
    

    


        
        