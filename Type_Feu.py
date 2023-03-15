from pokemon import Pokemon



class Feu(Pokemon):
    def __init__(self, nom, type, degat, defense):
        super().__init__(self, nom, type, degat, defense)
        self.modif_hp(15)
        self.degat += 20
        self.defense += 10



