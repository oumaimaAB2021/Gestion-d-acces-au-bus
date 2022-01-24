import itertools
#La classe Transition

class Transition():
    id= itertools.count(1)
    #Le constructeur de la classe
    def __init__(self,etatSource,alphabet,etatDestination):
        #Les attributs d'instance
        self.idTransition=next(self.id)
        self.etatSource=etatSource
        self.alphabet=alphabet
        self.etatDestination=etatDestination

    #Les accesseurs
    def get_idTransition(self):
        return self.idTransition

    def get_etatSource(self):
        return self.etatSource

    def get_etatDestination(self):
        return self.etatDestination

    def get_alphabet(self):
        return self.alphabet

    #Les manipulateurs
    def set_idTransition(self,idTransition):
        self.idTransition=idTransition

    def set_etatSource(self,etatSource):
        self.etatSource=etatSource

    def set_etatDestination(self,etatDestination):
        self.etatDestination=etatDestination

    def set_alphabet(self,alphabet):
        self.alphabet=alphabet

    #Méthode d'affichage
    def afficherTransition2(self):
        print("La transition :",end='\n')
        print("  d'id :",self.idTransition,end='\n')
        print("  de l'état source :",end='\n')
        self.etatSource.afficherEtat()
        print("  avec l'alphabet: ",)
        self.alphabet.afficherAlphabet()
        print("  et d'état destination :",end='\n')
        self.etatDestination.afficherEtat()

    def afficherTransition(self):
        print("  (", self.etatSource.afficherEtat(),',',self.alphabet.afficherAlphabet(),',',self.etatDestination.afficherEtat(),'),')