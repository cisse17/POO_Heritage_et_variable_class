

#          EtreVivant   =>   class parent
#    Chat   &  Personne  => classes enfant (ou classes dérivées )

# _______Reflexion________(Consigne)
#   Personne  (entité -> class)
#    Données : nom, age
#    Actions :  (méthodes)
#       - SePresenter()
#       - DemanderNom() / input

# nom : str
# age : int
# 1 - Si age == 0
#   => Bonjour, je m'appelle Toto
#   => On affiche pas mineur
# 2 - Si nom == ""
#   => Demander nom à l'utilisateur
#   => DemanderNom(...) -> input("") -> nom

#   POO EXERCICE DE MISE EN SITUATION 1
#   genre
#   False : Femme
#   True  : Homme
#   etudiant herite de personne
#   etre vivant


"""  exo POO   """


class EtreVivant:
    ETRE_VIVANT = "inconnu"

    def afficher_infos_etre_vivant(self):
        print("Etre vivant :", self.ETRE_VIVANT)

class Personne(EtreVivant):
    ETRE_VIVANT = "Humain"

    def __init__(self, nom, age, genre: bool = False):
        self.nom = nom
        self.age = age
        self.genre = genre
        if nom == "":
            self.demander_nom()

    def se_presenter(self):
        infos_personne = "Bonjour, je m'appelle " + self.nom + " j'ai " + str(self.age) + " ans"
        if self.age == 0:
            infos_personne = "Bonjour, je m'appelle " + self.nom
        print(infos_personne)

        genre = "Feminin"
        if self.genre:
           genre = "Masculin"
        print(f"Genre : {genre}")

        accord_de_e = "" if self.genre else "e"
        if self.age != 0:
            if self.est_majeur():
                print("Vous etes majeur"+accord_de_e)
            else:
                print("Vous etes mineur"+accord_de_e)
        # print("Infos etre vivant : ", Personne.ETRE_VIVANT)

    def demander_nom(self):
        self.nom = input("Quel est votre nom ? ")

    def est_majeur(self):
        return self.age >= 18


class Etudiant(Personne):
    def __init__(self, nom, age, genre, etudes):
        super().__init__(nom, age, genre)
        self.etudes = etudes

    def se_presenter(self):
        super().se_presenter()
        print(f"Etudes : Je suis étudiant en {self.etudes}")


class Chat(EtreVivant):
    ETRE_VIVANT = "Animal"

    def __init__(self, nom_chat):
        self.nom = nom_chat

    def se_presenter(self):
        print(f"Bonjour, je Suis un chat je m'appelle {self.nom}")
        # print("Infos etre vivant :", Chat.ETRE_VIVANT)


personne1 = Personne("Marie", 23)
personne2 = Personne("Bassirou", 16, True)
# personne2 = Personne()

liste_personne = (personne1, personne2)
for personne in liste_personne:
    personne.se_presenter()
    personne.afficher_infos_etre_vivant()
    print()

etudiant = Etudiant("Basse", 29, True, "école ingénieur")
etudiant.se_presenter()
etudiant.afficher_infos_etre_vivant()

print()
chat = Chat("Tomi")
chat.se_presenter()
chat.afficher_infos_etre_vivant()