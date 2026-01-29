import datetime

class Operazioni:

     def __init__(self,prestito,restituzione ):
           self.prestito
           self.restituzione
           self.data=datetime.now()
      

        
     def __repr__(self):
        return f" class operazioni : prestito {self.prestito} data:{self.data}, restituzione : {self.restituzione} data: {self.data}"
        
        
     def __eq__(self, other):
          if not isinstance (self,other):
           return False
          
          return self.prestito == other.prestito ,self.restituzione == other.restituzione and self.data== other.data
        
        
     def prestito(self):
         pass
     
     def restituzione(self):
         pass   
     

     def storico_restituzione(self):
         pass