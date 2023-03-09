from pokemon import Pokemon
from Type_Eau import Eau
from Type_Feu import Feu
from Type_Plante import Plante


class Normal(Pokemon):
    def __init__(self, nom, type, degat, defense):
        super().__init__(self, nom, type, degat, defense)

    def gettype(self):
        if self.type == Feu:
            self.degat = self.degat * 0.75
        if self.type == Eau:
            self.degat = self.degat * 0.75
        if self.type == Plante:
            self.degat = self.degat * 0.75
        elif self.type == Normal:
            self.degat = self.degat * 1