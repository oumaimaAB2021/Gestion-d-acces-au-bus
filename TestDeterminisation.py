from Etat import Etat
from Alphabet import Alphabet
from Transition import Transition
from Automate import Automate

#Si on veut introduire les automates de test à la main on décommente les 2 lignes suivantes

# donnee=Automate.lireAutomate()
# ListAutomate=list(donnee)


#Automate non deterministe

etat1=Etat("s1","initial")
etat2=Etat("s2","initial")
etat3=Etat("s3","intérmidiaire")
etat4=Etat("s4","final")
alphabet1=Alphabet("a")
alphabet2=Alphabet("b")
alphabet3=Alphabet("c")
transition1=Transition(etat1,alphabet1,etat1)
transition2=Transition(etat1,alphabet1,etat3)
transition3=Transition(etat2,alphabet2,etat2)
transition4=Transition(etat2,alphabet2,etat3)
transition5=Transition(etat3,alphabet3,etat3)
transition6=Transition(etat3,alphabet3,etat4)

etats=[etat1,etat2,etat3,etat4]

alpha=[alphabet1,alphabet2,alphabet3]

tran=[transition1,transition2,transition3,transition4,transition5,transition6]

initiaux=[etat1,etat2]
finaux=[etat4]


ListAFD=[alpha,etats,initiaux,finaux,tran]
automate=Automate.creationAutomate(ListAFD)

automate.afficherAutomate()

if(automate.isDeterministe()):
    print("L'automate est déterministe \n")
else:
    print("\n L'automate n'est pas déterministe \n")

automate.grapheAutomate("Automate finis non deterministe")


#Automate détérministe

etat1=Etat("s1","initial")
etat2=Etat("s2","final")
etat3=Etat("s1,s3","intérmidiaire")
etat4=Etat("s1,s4","intérmidiaire")
etat5=Etat("s1,s3,s4","intérmidiaire")
alphabet1=Alphabet("a")
alphabet2=Alphabet("b")

transition1=Transition(etat1,alphabet2,etat2)
transition2=Transition(etat1,alphabet1,etat3)
transition3=Transition(etat2,alphabet2,etat4)
transition4=Transition(etat3,alphabet2,etat2)
transition5=Transition(etat3,alphabet1,etat5)
transition6=Transition(etat4,alphabet2,etat2)
transition7=Transition(etat4,alphabet1,etat5)
transition8=Transition(etat5,alphabet2,etat2)
transition9=Transition(etat5,alphabet1,etat5)

etats=[etat1,etat2,etat3,etat4,etat5]

alpha=[alphabet1,alphabet2]

tran=[transition1,transition2,transition3,transition4,transition5,transition6,transition7,transition8,transition9]

initiaux=[etat1]
finaux=[etat2]

ListAFN=[alpha,etats,initiaux,finaux,tran]
automate2=Automate.creationAutomate(ListAFN)

automate2.afficherAutomate()

if(automate2.isDeterministe()):
    print("\n L'automate est déterministe \n")
else:
    print("\n L'automate n'est pas déterministe")
    
automate2.grapheAutomate("Automate finis deterministe")

#automate2.determiniserAutomate()