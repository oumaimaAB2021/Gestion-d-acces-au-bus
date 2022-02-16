#La classe Automate
from Etat import Etat
from Alphabet import Alphabet
from Transition import Transition

class Automate:
    #Le constructeur
    def __init__(self,listAlphabets,listEtats,listInitiaux,listFinaux,listTransitions):
        self.listAlphabets=listAlphabets
        self.listEtats=listEtats
        self.listInitiaux=listInitiaux
        self.listFinaux=listFinaux
        self.listTransitions=listTransitions

     #Les accesseurs
    def get_listAlphabets(self):
        return self.listAlphabets

    def get_listEtats(self):
        return self.listEtats

    def get_listInitiaux(self):
        return self.listInitiaux

    def get_listFinaux(self):
        return self.listFinaux

    def get_listTransitions(self):
        return self.listTransitions

    # Les manipulateurs
    def set_listAlphabets(self,listAlphabets):
        self.listAlphabets=listAlphabets

    def set_listEtats(self,listEtats):
        self.listEtats=listEtats

    def set_listInitiaux(self,listInitiaux):
        self.listInitiaux=listInitiaux

    def set_listFinaux(self,listFinaux):
        self.listFinaux=listFinaux

    def set_listTransitions(self,listTransitions):
        self.listTransitions=listTransitions

    #Lecture d'un automate
    def lireAutomate():
        donnée = input ("Merci d'introduire votre automate \n: ")
        #On transforme la donnée introduite en une liste
        automate=list(eval(donnée))
        alphabets=automate[0]            
        states=automate[1]
        listInitiale=automate[2]
        listFinale=automate[3]
        listTransitions=automate[4]
        #Construction de la liste des états
        etats=[]
        for e in states:
            if e in listInitiale:
                etat=Etat(e,'initiale')
            if e in listFinale:
                etat=Etat(e,'finale')
            else:
                etat=Etat(e,'intermediaire')
            etats.append(etat)
        #Construction de la liste des alphabets
        alpha=[]
        for a in alphabets:
            alphabet=Alphabet(a)
            alpha.append(alphabet)
        #Construction de la liste des transitions
        trans=[]
        for t in listTransitions:
            for e in etats:
                if (t[0]==e.labelEtat):
                    e1=e
                if(t[2]==e.labelEtat):
                    e2=e
            for a in alpha:
                if(t[1]==a.valAlphabet):
                    a1=a
            transition=Transition(e1,a1,e2)
            trans.append(transition)
        #Construction de la liste des états initiaux
        init=[]
        for i in listInitiale:
            initiale=Etat(i,'initiale')
            init.append(initiale)
         #Construction de la liste des états finaux
        fin=[]
        for j in listFinale:
            final=Etat(j,'finale')
            fin.append(final)
        return alpha,etats,init,fin,trans
    
    #Creation d'un automate
    def creationAutomate(L):
        alphabets=L[0]
        states=L[1]
        listInitiale=L[2]
        listFinale=L[3]
        transitions=L[4]
        return Automate(alphabets,states,listInitiale,listFinale,transitions)

    
    #La méthode d'affichage
    def afficherAutomate(self):
        print("\n Les éléments de l'automate :",end='\n \n')
        print('[',end='')
        Alphabets=[]
        for i in range(len(self.listAlphabets)) :
            Alphabets.append(self.listAlphabets[i].afficherAlphabet())
        print(Alphabets,',')
        Etats=[]
        for i in range(len(self.listEtats)) :
            Etats.append(self.listEtats[i].afficherEtat())
        print('  ',Etats,',')
        EtatsInitiaux=[]
        for i in range(len(self.listInitiaux)) :
            EtatsInitiaux.append(self.listInitiaux[i].afficherEtat())
        print('  ',EtatsInitiaux,',')
        EtatsFinaux=[]
        for i in range(len(self.listFinaux)) :
            EtatsFinaux.append(self.listFinaux[i].afficherEtat())
        print('  ',EtatsFinaux,',')
        print("  [", end=" ")
        for i in range(len(self.listTransitions)):
            self.listTransitions[i].afficherTransition()
        print('  ',"]")
        print(' ',"]")


    #Les méthodes d'ajout

    def ajouterAlphabet(self,alphabet):
        self.listAlphabets.append(alphabet)

    def ajouterEtat(self,etat):
        if etat in self.listEtats :
            print('Cet état existe dèjà ! Essayez avec une autre')
        else:
             self.listEtats.append(etat)

    def ajouterEtatInitial(self,etat):
        existe=True
        self.listInitiaux.append(etat)
        #Vérification de l'existence de l'état dans la liste globale
        for i in range(len(self.listEtats)):
            if(self.listEtats[i]==etat):
                existe=False
                break
        if(existe):
            self.listEtats.append(etat)

    def ajouterEtatFinal(self,etat):
        existe=True
        self.listFinaux.append(etat)
        for i in range(len(self.listEtats)):
            if(self.listEtats[i]==etat):
                existe=False
                break
        if(existe):
            self.listEtats.append(etat)

    def ajouterTransition(self,transition):
        self.listTransitions.append(transition)

  # Recherche des élèments par ID

  #Recherche d'un état par son id
    def findEtatById(self,id):
        etat=None
        for element in self.listEtats:
            if element.get_idEtat()==id:
                etat=element
                break
        return etat

   #Recherche d'un alphabet par son id
    def findAlphabetById(self,id):
        alphabet=None
        for element in self.listAlphabets:
            if element.get_idAlphabet()==id:
               alphabet=element
               break
        return alphabet

    #Recherche d'une transition par son id
    def findTransitionById(self,id):
         transition=None
         for element in self.listTransitions:
             if element.get_idTransition()==id:
                transition=element
                break
         return transition

    #Recherche d'une transition par état
    def findTransitionsByEtat(self,etat):
         transition=[]
         for element in self.listTransitions:
             if (element.get_etatSource()==etat or element.get_etatDestination()==etat) :
                transition.append(element)
         return transition

     #Recherche d'une transition par un alphabet
    def findTransitionsByAlphabet(self,alphabet):
          transition=[]
          for element in self.listTransitions:
              if (element.get_alphabet()==alphabet) :
                 transition.append(element)
          return transition

    #Les méthodes de suppression

    def supprimerEtat(self,idEtat):
        etat=self.findEtatById(idEtat)
        self.listEtats.remove(etat)
        transitions=self.findTransitionsByEtat(etat)
        for t in transitions:
            self.listTransitions.remove(t)

    def supprimerEtatInitial(self,idEtatInitial):
        etat=self.findEtatById(idEtatInitial)
        self.listInitiaux.remove(etat)
        transitions=self.findTransitionsByEtat(etat)
        for t in transitions:
            self.listTransitions.remove(t)

    def supprimerEtatFinal(self,idEtatFinal):
        etat=self.findEtatById(idEtatFinal)
        self.listFinaux.remove(etat)
        transitions=self.findTransitionsByEtat(etat)
        for t in transitions:
            self.listTransitions.remove(t)

    def supprimerAlphabet(self,idAlphabet):
        alphabet=self.findAlphabetById(idAlphabet)
        self.listAlphabets.remove(alphabet)
        transitions=self.findTransitionsByAlphabet(alphabet)
        for t in transitions:
            self.listTransitions.remove(t)

    def supprimerTransition(self,idTransition):
        transition=self.findTransitionById(idTransition)
        self.listTransitions.remove(transition)

    #Les méthodes de modification
    def modifierEtat(self,idEtat,NouveauEtat):
        #Cette méthode permet de modifier l'état partout que ce soit liste des états ou
        #liste des transitions
        etat=self.findEtatById(idEtat)
        etat.set_idEtat(NouveauEtat.idEtat)
        etat.set_labelEtat(NouveauEtat.labelEtat)
        etat.set_typeEtat(NouveauEtat.typeEtat)

    def modifierEtatInitial(self,idEtatInitial,NouveauEtat):
        etatInitial=self.findEtatById(idEtatInitial)
        etatInitial.set_idEtat(NouveauEtat.idEtat)
        etatInitial.set_labelEtat(NouveauEtat.labelEtat)
        etatInitial.set_typeEtat(NouveauEtat.typeEtat)

    def modifierEtatFinal(self,idEtatFinal,NouveauEtat):
        etatFinal=self.findEtatById(idEtatFinal)
        etatFinal.set_idEtat(NouveauEtat.idEtat)
        etatFinal.set_labelEtat(NouveauEtat.labelEtat)
        etatFinal.set_typeEtat(NouveauEtat.typeEtat)

    def modifierAlphabet(self,idAlphabet,NouveauAlphabet):
       alphabet=self.findAlphabetById(idAlphabet)
       alphabet.set_idAlphabet(NouveauAlphabet.idAlphabet)
       alphabet.set_valAlphabet(NouveauAlphabet.valAlphabet)

    def modifierTransition(self,idTransition,NouveauTransition):
       transition=self.findTransitionById(idTransition)
       transition.set_idTransition(NouveauTransition.idTransition)
       transition.set_etatSource(NouveauTransition.etatSource)
       transition.set_etatDestination(NouveauTransition.etatDestination)
       transition.set_alphabet(NouveauTransition.alphabet)

    #Vérification d'un automate si il est determiiste ou non
    def isDeterministe ( automate ) :
        deterministe = True
        if (len(automate.listInitiaux)!=1):
            deterministe=False
        else:
            transitions = automate.listTransitions
            for t in transitions :
                s = t.etatSource.labelEtat
                a = t.alphabet.valAlphabet
                compteur=0
                for i in transitions :
                    if i.etatSource.labelEtat == s and i.alphabet.valAlphabet == a :
                        compteur+= 1
                    if compteur >1:
                        deterministe = False
                        break
        return deterministe

#But: On cherche les destinations de l'état source en utilisant la trasition étiquettée par alphabet
    def findDestination(self,etatSource,alphabet):
            destination=[]
            for element in self.listTransitions:
                if (element.etatSource.labelEtat==etatSource and element.alphabet.valAlphabet==alphabet) :
                    if(not element.etatDestination.labelEtat in destination):
                        destination.append(element.etatDestination.labelEtat)
            return destination

#Déterminisation d'un automate
    def determiniserAutomate(self,automate):
        if(automate.isDeterministe()):
            print("Cet automate est déjà déterministe")
        else:
            print("Cet automate n'est pas déterministe! Il faut la rendre deterministe")
            transitions=self.listTransitions
            #On rassemble les états initiaux de l'AFN
            newEtatInitial=[]
            for i in range(len(self.listInitiaux)):
                newEtatInitial.append(self.listInitiaux[i].labelEtat)
            print("initial",newEtatInitial)
            # Construction de la table des transitions
            destinations=[]
            destinations2=[]
            for t in transitions:
                for i in newEtatInitial:
                    dests=self.findDestination(i, t.alphabet.valAlphabet)
                    if(dests!=[]):
                        destinations=dests
                        #print("A partir de ",newEtatInitial,"on peut atteindre",destinations,"par l'alphabet:",t.alphabet.valAlphabet)
                for d in destinations:
                    dests2=self.findDestination(d, t.alphabet.valAlphabet)
                    if(dests2!=[]):
                        if(dests2 not in destinations2):
                            #print("Les destinations2 de l'état:",d,"par l'alphabet:",t.alphabet.valAlphabet,"sont:",dests2)
                            destinations2.append(dests2)
            newlistEtats=[newEtatInitial]
            newlistEtats+=[destinations]
            for i in range(len(destinations2)):
                #print("destinations2 non list",destinations2[i])
                newlistEtats+=[destinations2[i]]
            print("nouvelle liste d'état***** \n",newlistEtats)
            # newlistTransitions=[]
            # newLabel=""
            # for t in transitions:
            #     destinations=self.findDestination(t.etatSource.labelEtat, t.alphabet.valAlphabet)
            #     print("Les destinations de l'état:",t.etatSource.labelEtat,"par l'alphabet:",t.alphabet.valAlphabet,"sont:",destinations)
            #     if(len(destinations)>1):
            #         for d in range(len(destinations)):
            #             newLabel=t.etatSource.labelEtat+","+t.etatDestination.labelEtat
            #             #newLabel+=destinations[d]
            #         newEtat=Etat(16,newLabel,'intermédiaire')
            #         newTransition=Transition(16,t.etatSource,t.alphabet,newEtat)
            #         newlistEtats.append(newEtat)
            #         newlistTransitions.append(newTransition)s
            #Création d'un nouveau automate après determinisation
            #newAutomate=Automate(self.listAlphabets,newlistEtats,newEtatInitial,self.listFinaux,newlistTransitions)
            #return newAutomate

    #Recherche d'une transition par un alphabet et un état à utiliser dans complet
    def findTransitionsByAlphabetEtat(self,alphabet,etat):
        transition=[]
        for element in self.listTransitions:
            if (element.get_alphabet()==alphabet and element.get_etatSource()==etat) :
                transition.append(element)
        return transition
    #Vérification de complétude
    #Je dois chercher les transitions sortantes de chaque état pour chaque alphabet
    def isComplet(automate):
        Complet = True
        etats = automate.listEtats
        alphabets=automate.listAlphabets
        for e in etats:
            for a in alphabets:
                transition=automate.findTransitionsByAlphabetEtat(a,e)
                if(len(transition)==0):
                    Complet = False
                    break
        return Complet
    
#Recherche des transitions d'un état source
    def findTransitionBySource(self,etat):
        transitions=[]
        for tr in self.get_listTransitions():
            if tr.get_etatSource()==etat:
                transitions.append(tr)
        return transitions


#Rendre un automate non complet complet
    def Completude(self,automate):
        if(automate.isComplet()):
            print("L'automate introduit est complet")
        else:
            #On crée un état puits
            P=Etat("P","puits")
            #Création de nouvel état à partir des transitions
            for a in self.listAlphabets:
                T=Transition(P,a,P)
                self.ajouterTransition(T)
            for e in self.listEtats:
                Tr=self.findTransitionBySource(e)
                L=[]
                for i in range(0,len(Tr)):
                    #Extraction de tous les alphabets associé aux transitions
                    L.append(Tr[i].get_alphabet())
                #Recherche des alphabets qui sont dans la liste des alphabets mais
                #ne figure pas dans la liste trouvé
                for j in self.listAlphabets:
                    if(j not in L):
                        New_Transition=Transition(e,j,P)
                        self.ajouterTransition(New_Transition)
                        
                        
        
#Affichage graphique
    def grapheAutomate(self,filename):
        #Importation de librairie
        import graphviz as gv
        #Création de la table
        graphe = gv.Digraph("Graphe d'un automate fini", filename)
        taille_listetransitions=len(self.listTransitions)
        #Création des noeuds des états
        for i in range(taille_listetransitions):
            graphe.node(self.listTransitions[i].get_etatSource().get_labelEtat(),self.listTransitions[i].get_etatSource().get_labelEtat())
        #Création des transitions
        for i in range(taille_listetransitions):
            graphe.edge(self.listTransitions[i].get_etatSource().get_labelEtat(), self.listTransitions[i].get_etatDestination().get_labelEtat(),label=self.listTransitions[i].get_alphabet().get_valAlphabet())
            graphe.attr('node', shape='doublecircle')
        #Visualisation du résultat graphique en format 'png'
        source=gv.Source(graphe)
        source.format='png'
        source.render(filename, view=False) 
        #graphe.view()

