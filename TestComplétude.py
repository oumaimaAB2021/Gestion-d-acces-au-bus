from Etat import Etat
from Alphabet import Alphabet
from Transition import Transition
from Automate import Automate

#Test d'un automate non complet

etat1=Etat("s1","initial")
etat2=Etat("s2","final")

alphabet1=Alphabet("a")
alphabet2=Alphabet("b")

transition1=Transition(etat1,alphabet1,etat1)
transition2=Transition(etat1,alphabet1,etat2)
transition3=Transition(etat2,alphabet2,etat2)
transition4=Transition(etat1,alphabet2,etat2)

etats=[etat1,etat2]
alpha=[alphabet1,alphabet2]
tran=[transition1,transition2,transition3,transition4]
initiaux=[etat1]
finaux=[etat2]

#Si on veut introduire les automates de test à la main on décommente les 2 lignes suivantes

# donnee=Automate.lireAutomate()
# ListAutomate=list(donnee)

ListAutomate=[alpha,etats,initiaux,finaux,tran]
automate=Automate.creationAutomate(ListAutomate)

print("*******Test de complétude******")
automate.afficherAutomate()
if(automate.isComplet()):
    print("\n L'automate a est complet")
else:
    print("\n l'automate a n'est pas complet \n")
automate.grapheAutomate("Automate finis non complet")

#Test Automate Complet
etat3=Etat("s1","initial")
etat4=Etat("s2","final")

alphabet3=Alphabet("a")
alphabet4=Alphabet("b")

transition5=Transition(etat3,alphabet3,etat3)
transition6=Transition(etat3,alphabet4,etat4)
transition7=Transition(etat4,alphabet4,etat4)
transition8=Transition(etat4,alphabet3,etat3)

etats2=[etat3,etat4]
alpha2=[alphabet3,alphabet4]
tran2=[transition5,transition6,transition7,transition8]
initiaux2=[etat3]
finaux2=[etat4]

ListAutomate2=[alpha2,etats2,initiaux2,finaux2,tran2]
automate2=Automate.creationAutomate(ListAutomate2)

automate2.afficherAutomate()
if(automate2.isComplet()):
    print("\n L'automate b est complet")
else:
    print("\n L'automate b n'est pas complet")
automate2.grapheAutomate("Automate finis complet")

#On complète l'automate qui n'est pas complet

automate.Completude(automate)
print("\n ***********Après complétude de a************ \n")
automate.afficherAutomate()
automate.grapheAutomate("Automate finis après complétude")
if(automate.isComplet()):
     print("L'automate est complet")
else:
     print("l'automate n'est pas complet")