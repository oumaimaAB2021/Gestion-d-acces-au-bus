# [['a','b','c','d','e'],
#   [1,2,3,4,5,6],
# [1,3,6],[6],
# [(1,'a',2),(1,'a',4),
#   (2,'a',2),(2,'c',5),
#   (2,'d',5),(3,'b',4),
#   (4,'b',4),(4,'c',5),
#   (4,'d',5),(5,'e',6)]]

#Importation des classes
from Etat import Etat
from Alphabet import Alphabet
from Transition import Transition
from Automate import Automate

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

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


automateApplication=[alpha,etats,initiaux,finaux,tran]
automate=Automate.creationAutomate(automateApplication)
#Création d'une fenetre
window =Tk()
#Personalisation
window.title("CasaBus -Automate")
window.geometry("960x660")
#window.minsize(480, 360)
window.resizable(width=False,height=False) #Interdire le redimentionnement
window.iconbitmap('Logo.ico')
window.config(background='#F7BE00')

frame=Frame(window,bg='#F7BE00')
label_title=Label(window, text="Gestion d'accès au Bus", font=("courrier",20),bg='#F7BE00',fg='#514D4D')
label_title.pack()
# label_subtitle=Label(frame, text="Automate de gestion d'acces au Bus", font=("courrier",14),bg='#F7BE00',fg='#514D4D')
# label_subtitle.pack()
#Afficher=Button(window, text ='Affichage graphique',command=automate.grapheAutomate("Graphe GUI"))
#Afficher.pack()
frame.pack(expand=YES)

# def recupere():
#     messagebox.showinfo("Alerte", donnee.get())
    

# value = StringVar() 
# value.set("Merci d'introduire votre automate:")
# donnee = Entry(window, textvariable=value, width=80)
# donnee.pack()

canvas=Canvas(window, width=550, height=540, bg='white')
canvas.pack()
defaultimage = Image.open("ValideCarte.jpeg")
# Resize the image using resize() method
resize_defaultimage =defaultimage.resize((550, 540))
#Intégrer une image
imgdefault = ImageTk.PhotoImage(resize_defaultimage)
canvas.create_image(0, 0, anchor=NW, image=imgdefault)

automate.grapheAutomate("Graphe GUI")
image = Image.open("Graphe GUI.png")
# Resize the image using resize() method
resize_image = image.resize((550, 540))
#Intégrer une image
img = ImageTk.PhotoImage(resize_image)

def show():    
    canvas.create_image(0, 0, anchor=NW, image=img)

btn=Button(frame, text ="Affichage graphique de l'automate",command=show).pack(side=TOP, padx=5, pady=5)

def complet():
    if (automate.isComplet()):
        Message="L'automate est complet"
    else: 
        Message="L'automate n'est pas complet! il faut le compléter"
    messagebox.showinfo("Alerte", Message)

def deterministe():
    if (automate.isDeterministe()):
        Message="L'automate est deterministe"
    else: 
        Message="L'automate n'est pas deterministe! il faut le determiniser"
    messagebox.showinfo("Alerte", Message)



def completer():
    #automate2=automate.Completude(automate)
    #automate2.grapheAutomate("Graphe GUI Complet")
    image2 = Image.open("AF d'application après complétude.png")
    # Resize the image using resize() method
    resize_image2 = image2.resize((550, 520))
    #Intégrer une image
    img2 = ImageTk.PhotoImage(resize_image2)
    canvas.create_image(10, 0, anchor=NW, image=img2)
    messagebox.showinfo("Alerte", "Le processus de complétude est fait avec succés")
        
    
# automate.supprimerEtat(etat3.idEtat)
# automate.grapheAutomate("Automate finis sans état 3")
# # Read the Image
# images = Image.open("Automate finis sans état 3.png")
# resize_images = images.resize((550, 500))
# imgs = ImageTk.PhotoImage(resize_images)
# def supprimerE():
#     canvas.create_image(10, 0, anchor=NW, image=imgs)
#     messagebox.showinfo("Alerte", "L'état 3 est supprimé avec succès ")

automate.modifierEtatInitial(etat1.idEtat,etat3)
automate.grapheAutomate("Automate finis modif 1")

# Read the Image
imagem = Image.open("Automate finis modif 1.png")
resize_imagem = imagem.resize((550, 500))
imgm = ImageTk.PhotoImage(resize_imagem)


def modifierE():
    canvas.create_image(0, 0, anchor=NW, image=imgm)
    messagebox.showinfo("Alerte", "L'état 1 est modifié avec succès ")


Button(frame, text ='Ajouter etat').pack(side=LEFT, padx=5, pady=5)
Button(frame, text ='Ajouter transition').pack(side=LEFT, padx=5, pady=5)

Button(frame, text ='Supprimer etat').pack(side=LEFT, padx=5, pady=5)
Button(frame, text ='Supprimer transition').pack(side=RIGHT, padx=5, pady=5)

Button(frame, text ='Modifier état',command=modifierE).pack(side=RIGHT, padx=5, pady=5)
Button(frame, text ='Test de complétude',command=complet).pack(side=LEFT, padx=5, pady=5)
Button(frame, text ='Test de determinisation',command=deterministe).pack(side=LEFT, padx=5, pady=5)
Button(frame, text ="Compléter l'automate",command=completer).pack(side=LEFT, padx=5, pady=5)



# #Input
# value = StringVar() 
# value.set("[['a','b','c','d','e'],[1,2,3,4,5,6],[1,3,6],[6],[(1,'a',2),(1,'a',4),(2,'a',2),(2,'c',5),(2,'d',5),(3,'b',4),(4,'b',4),(4,'c',5),(4,'d',5),(5,'e',6)]]")
# donnee = Entry(window, textvariable=value, width=80)
# donnee.pack()

# def recupere():
#     automate=donnee.get()
#     return automate

# Myautomate=recupere()
# print("Liste",Myautomate)

# def lireAutomate(Myautomate):
#     automate=list(Myautomate) 
#     alphabets=automate[0]          
#     states=automate[1]
#     listInitiale=automate[2]
#     listFinale=automate[3]
#     listTransitions=automate[4]
#     #Construction de la liste des états
#     etats=[]
#     for e in states:
#         if e in listInitiale:
#             etat=Etat(e,'initiale')
#         if e in listFinale:
#             etat=Etat(e,'finale')
#         else:
#             etat=Etat(e,'intermediaire')
#         etats.append(etat)
#   #Construction de la liste des alphabets
#     alpha=[]
#     for a in alphabets:
#         alphabet=Alphabet(a)
#         alpha.append(alphabet)
#     #Construction de la liste des transitions
#     trans=[]
#     for t in listTransitions:
#           for e in etats:
#               if (t[0]==e.labelEtat):
#                   e1=e
#               if(t[2]==e.labelEtat):
#                   e2=e
#           for a in alpha:
#               if(t[1]==a.valAlphabet):
#                   a1=a
#           transition=Transition(e1,a1,e2)
#           trans.append(transition)
#       #Construction de la liste des états initiaux
#     init=[]
#     for i in listInitiale:
#         initiale=Etat(i,'initiale')
#         init.append(initiale)
#       #Construction de la liste des états finaux
#     fin=[]
#     for j in listFinale:
#         final=Etat(j,'finale')
#         fin.append(initiale)
#     return alpha,etats,init,fin,trans


# def creerAutomate():
#     entree=lireAutomate(Myautomate)
#     ListAutomate=list(entree)
#     automate=Automate.creationAutomate(ListAutomate)
#     print('bien créer')



# bouton = Button(window, text="Valider", command=creerAutomate)
# bouton.pack()



#Affichage
window.mainloop()


