# Project réalisé lors de mon apprentissage Programmation Orientée Object
# #   _________EXERCICE POO___________
    Personne  (entité -> class)
    Données : nom, age
    Actions :  (méthodes)
       - SePresenter()
       - DemanderNom() / input

     nom : str
     age : int
     1 - Si age == 0
       => Bonjour, je m'appelle Toto
       => On affiche pas mineur
     2 - Si nom == ""
       => Demander nom à l'utilisateur
       => DemanderNom(...) -> input("") -> nom
    
     POO EXERCICE DE MISE EN SITUATION 1
     genre
       False : Femme
       True  : Homme
       etudiant herite de personne
       etre vivant
