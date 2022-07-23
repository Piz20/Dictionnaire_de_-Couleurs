from tkinter import *


def findKey(valeur, dictionnaire):
    for k, val in dictionnaire.items():
        if valeur == val:
            return k


class Application(Frame):
    """fenêtre d'application"""
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Création d'un dictionnaire de couleurs")
        self.dico = {}

        frSup = Frame(self)
        frSup.pack(padx=5, pady=5)
        Label(frSup,text="Nom de la couleur :",width=20).grid(row=1 ,column=1)
        self.couleur = Entry(frSup,width=25)
        self.couleur.grid(row=1, column=2)

        Label(frSup, text="Code hexa. corresp. :",width =20).grid(row =2, column =1)
        self.code = Entry(frSup, width=25)
        self.code.grid(row=2, column=2)
        Button(frSup, text="Test", width=12,
               command=self.retrouveCode).grid(row=2, column=3)
        Button(frSup, text="Existe déjà ?", width=12,
               command=self.chercheCoul).grid(row=1, column=3)


        frInf = Frame(self)
        self.test = Label(frInf, bg="white", width=45,
                          height=7, relief=SUNKEN)
        self.test.pack(pady=5)
        Button(frInf, text="Ajouter la couleur au dictionnaire",
               command=self.encodage).pack()
        Button(frInf, text="Enregistrer le dictionnaire", width=25,
               command=self.sauvegarder).pack(side=LEFT, pady=5)
        Button(frInf, text="Restaurer le dictionnaire", width=25,
               command=self.recons).pack(side=RIGHT, pady=5)
        frInf.pack(padx=5, pady=5)
        self.pack()

        self.recons()

    def chercheCoul(self):
        nom = self.couleur.get()
        if nom in self.dico:
            self.test.config(bg=self.dico[nom], text="")
        else:
            self.test.config(text="%s : couleur inconnue" % nom, bg='white')

    def encodage(self):

        self.codex = self.code.get()
        self.coul = self.couleur.get()
        self.coul.lower()
        self.dico[self.coul] = self.codex
        self.code.delete(0, END)
        self.couleur.delete(0, END)
        print(self.dico)

    def sauvegarder(self):
        of = open("dictionnairedecouleurs.txt", 'w')
        for self.coul in self.dico:
            ch = "{0}@{1}".format(self.coul, self.dico[self.coul])
            of.write(ch + "\n")
        of.close()

    def recons(self):
        try:
            of = open("dictionnairedecouleurs.txt", 'r')
            while 1:
                chaine = of.readline()
                if chaine == '':
                    break
                enreg = chaine.split("@")
                self.coul = enreg[0]
                self.codex = enreg[1][:-1]
                self.dico[self.coul] = self.codex
            print(self.dico)
            of.close()
        except:
            pass

    def retrouveCode(self):
        try:
            self.coul = self.couleur.get().lower()
            self.code.delete(0, END)
            self.code.insert(END, self.dico[self.coul])
            self.test.configure(bg=self.dico[self.coul])
        except:
            self.signalErreur(self.couleur)

    def signalErreur(self, champ):
        self.champ = champ
        self.champ.configure(bg='red')
        self.after(2000, self.videEntree)

    def videEntree(self):
        self.champ.configure(bg="white")
        self.champ.delete(0, END)


if __name__ == "__main__":
    Application().mainloop()
