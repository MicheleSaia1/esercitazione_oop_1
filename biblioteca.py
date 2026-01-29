class Biblioteca:
    
    
    
     def __init__(self,utente,libri,):
           self.utente=utente
           self.libri=[]
           self.disponibilita= True
        
       

        
     def __repr__(self):
           return f"classe biblioteca: utente: {self.utente} , libri : {self.libri} , disponibilità: {self.disponibilità}"
        
            
            
     def __eq__(self, other):
             if not isinstance(self,other):
              return False
             
             return self.utente == other.utente, self.libri == other.libri, self.disponibilita == other.disponibilita
    

     def aggiunta_nuovi_libri(self,libri):
        if libri  in self.aggiunta_nuovi_libri:
            print(" il libro è già registrato")
            return False
        
        if # condizione per aggiungere in libri=[] (.append)
            return True


          

     def ricerca_dei_libri(self):
      pass

     
     def libri_diponibili(self):
          pass
     

     
          
      
            

    