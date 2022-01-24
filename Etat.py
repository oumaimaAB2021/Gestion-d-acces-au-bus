import itertools 
#La classe Etat
class Etat:
    #Le constructeur de la classe
    #__init__(): est une méthode d'initialisation
    id= itertools.count(1)
    def __init__(self,labelEtat,typeEtat):
        #Les attributs d'instance
        self.idEtat=next(self.id)
        self.labelEtat=labelEtat
        self.typeEtat=typeEtat

    #Les accesseurs
    def get_idEtat(self):
        return self.idEtat

    def get_labelEtat(self):
        return self.labelEtat

    def get_typeEtat(self):
        return self.typeEtat

    #Les manipulateurs
    def set_idEtat(self,idEtat):
        self.idEtat=idEtat

    def set_labelEtat(self,labelEtat):
        self.labelEtat=labelEtat
        

    def set_typeEtat(self,typeEtat):
        self.typeEtat=typeEtat

    #La méthode d'affichage
    def afficherEtat2(self):
        print(" L'état d'id : ",self.idEtat," est etiquettée par : ",self.labelEtat," de type : ",self.typeEtat)

    def afficherEtat(self):
        return self.labelEtat