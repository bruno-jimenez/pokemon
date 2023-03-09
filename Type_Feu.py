from pokemon import Pokemon
from Type_Eau import Eau
from Type_Plante import Plante
from Type_Normal import Normal


class Feu(Pokemon):
    def __init__(self, nom, type, degat, defense):
        super().__init__(self, nom, type, degat, defense)
        self.modif_hp(15)
        self.degat += 20
        self.defense += 10

    def gettype(self):
        if self.type == Feu:
            self.degat = self.degat * 1
        if self.type == Eau:
            self.degat = self.degat * 0.5
        if self.type == Normal:
            self.degat = self.degat * 1
        elif self.type == Plante:
            self.degat = self.degat * 2

