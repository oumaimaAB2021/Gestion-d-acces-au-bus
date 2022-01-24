from Etat import Etat
from Alphabet import Alphabet
from Transition import Transition
from Automate import Automate


etat1=Etat("Barre Bloquée","initial et final")
etat2=Etat("Barre Débloquée","intérmidiaire")
etat3=Etat("Ticket Sortie","intérmidiaire")
etat4=Etat("Tapis Ouvert","intérmidiaire")
etat5=Etat("Tapis Fermé","initial et final")


alphabet1=Alphabet("Solde")
alphabet2=Alphabet("Temps dépassé")
alphabet3=Alphabet("Bouton: Ticket")
alphabet4=Alphabet("Bouton: Handicapé")
alphabet5=Alphabet("Pénétration")

transition1=Transition(etat1,alphabet1,etat2)
transition2=Transition(etat1,alphabet4,etat4)
transition3=Transition(etat2,alphabet2,etat1)
transition4=Transition(etat2,alphabet3,etat3)
transition5=Transition(etat3,alphabet5,etat1)
transition6=Transition(etat3,alphabet5,etat5)
transition7=Transition(etat4,alphabet1,etat2)

etats=[etat1,etat2,etat3,etat4,etat5]
alpha=[alphabet1,alphabet2,alphabet3,alphabet4,alphabet5]
tran=[transition1,transition2,transition3,transition4,transition5,transition6,transition7]
initiaux=[etat1,etat5]
finaux=[etat1,etat5]

automate=Automate(alpha,etats,initiaux,finaux,tran)


print("\n*************Affichage de l'automate**********\n")
automate.afficherAutomate()

#Affichage graphique
automate.grapheAutomate("Automate finis")


# print("\n*************Vérification de déterminisation**********\n")
# if(automate.isDeterministe()):
#     print("L'automate  est déterministe")
# else:
#     print("l'automate n'est pas déterministe")
    
    
# print("\n*************Vérification de complétude**********\n")

# if(automate.isComplet()):
#     print("L'automate est complet")
# else:
#     print("l'automate n'est pas complet")
    
automate.Completude(automate)

print("\n*************Affichage après complétude**********\n")
automate.afficherAutomate()

if(automate.isComplet()):
      print("L'automate est complet")
else:
      print("l'automate n'est pas complet")
     

#Affichage graphique après complétude
automate.grapheAutomate("AF d'application après complétude")