import random 


class Pokemon:

    def __init__(self, nom, type, vie, degat, defense):
        self.nom = nom
        self.vie = vie
        self.degat = degat
        self.type = type
        self.defense = defense

    def information(self):
        print(f"Pokmemon :",self.nom)
        print(f"Type :",self.type)
        print(f"PV :",self.vie)
        print(f"Attaque :",self.degat)
        print(f"Defense :",self.defense)


'''class Combat:

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tour = 1

    def alive(self):
        if self.vie > 0:
            print(self.nom ,"K.O")
        else: 
            pass

    def attack(self):
        resultat = random.randint(0, 1)
        if resultat == 1:
            self.degat '''

pokemon1 = Pokemon("Girania", "spectre", 130, 20, 13 )
pokemon1.information()