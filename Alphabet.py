import itertools 
#La classe Alphabet
class Alphabet():
    id= itertools.count(1)
    def __init__(self,valAlphabet):
        self.idAlphabet=next(self.id)
        self.valAlphabet=valAlphabet

     #Les accesseurs
    def get_idAlphabet(self):
        return self.idAlphabet

    def get_valAlphabet(self):
        return self.valAlphabet

    #Les manipulateurs
    def set_idAlphabet(self,idAlphabet):
        self.idAlphabet=idAlphabet

    def set_valAlphabet(self,valAlphabet):
        self.valAlphabet=valAlphabet

    #La méthode d'affichage
    def afficherAlphabet2(self):
        print("(",self.idAlphabet,",",self.valAlphabet,")")

    def afficherAlphabet(self):
        return self.valAlphabet
    
