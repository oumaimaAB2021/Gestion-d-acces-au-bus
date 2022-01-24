from Etat import Etat
from Alphabet import Alphabet
from Transition import Transition
from Automate import Automate


etat1=Etat("s1","initial")
etat2=Etat("s2","intérmidiaire")
etat3=Etat("s3","initial")
etat4=Etat("s4","intérmidiaire")
etat5=Etat("s5","intérmidiaire")
etat6=Etat("s6","initial et final")

alphabet1=Alphabet("a")
alphabet2=Alphabet("b")
alphabet3=Alphabet("c")
alphabet4=Alphabet("d")
alphabet5=Alphabet("e")

transition1=Transition(etat1,alphabet1,etat2)
transition2=Transition(etat1,alphabet1,etat4)
transition3=Transition(etat2,alphabet1,etat2)
transition4=Transition(etat2,alphabet3,etat5)
transition5=Transition(etat2,alphabet4,etat5)
transition6=Transition(etat3,alphabet2,etat2)
transition7=Transition(etat3,alphabet2,etat4)
transition8=Transition(etat4,alphabet2,etat4)
transition9=Transition(etat4,alphabet3,etat5)
transition10=Transition(etat4,alphabet4,etat5)
transition11=Transition(etat5,alphabet5,etat6)

etats=[etat1,etat2,etat3,etat4,etat5,etat6]
alpha=[alphabet1,alphabet2,alphabet3,alphabet4,alphabet5]
tran=[transition1,transition2,transition3,transition4,transition5,transition6,transition7,transition8,transition9,transition10,transition11]
initiaux=[etat1,etat3,etat6]
finaux=[etat6]

ListAF=[alpha,etats,initiaux,finaux,tran]
automate=Automate.creationAutomate(ListAF)

#automate.afficherAutomate()
#print('\n ************Après ajout********************* \n')
##alphabet6=Alphabet("f")
##automate.ajouterAlphabet(alphabet6)
#
##etat7=Etat("s8","intérmidiaire")
##automate.ajouterEtatInitial(etat7)
#
##etat8=Etat("s8","initial")
##automate.ajouterEtatInitial(etat8)
#
##etat9=Etat("s9","final")
##automate.ajouterEtatFinal(etat9)
#
#transition12=Transition(etat6,alphabet2,etat5)
#automate.ajouterTransition(transition12)
#automate.afficherAutomate()

#automate.afficherAutomate()
#print('\n ************Apres suppression******** \n')
#automate.supprimerAlphabet(2)
#automate.supprimerEtat(2)
#automate.supprimerEtatInitial(1)
#automate.supprimerEtatFinal(6)
#automate.supprimerTransition(4)
#automate.afficherAutomate()


automate.afficherAutomate()
automate.grapheAutomate("Automate finis avant modification")

print('\n ************Apres modification******** \n')
#automate.modifierAlphabet(2,alphabet3)
#automate.modifierEtat(1,etat5)
automate.modifierEtatInitial(1,etat5)
#automate.modifierEtatFinal(6,etat5)
#automate.modifierTransition(1,transition3)
automate.afficherAutomate()
automate.grapheAutomate("Automate finis après modification")










