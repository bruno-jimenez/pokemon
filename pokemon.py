class Pokemon:

    def __init__(self, nom, type, degat, defense):
        self.__nom = nom
        self.__vie = 100
        self.degat = degat
        self.type = type
        self.defense = defense


    '''def information(self):
        print(f"Pokmemon :",self.__nom)
        print(f"Type :",self.type)
        print(f"PV :",self.__vie)
        print(f"Attaque :",self.degat)
        print(f"Defense :",self.defense)'''


    def name(self): 
        return self.__nom

    def hp(self): 
        return self.__vie
    
    def modif_pv(self, newpv):
        self.__pv += newpv
    
    def set_pv(self, newpv):
        self.__pv -= newpv

    def attaquer(self):
       print(self.__nom, 'attaque', self.degat)


'''pokemon = Pokemon("Girania", "spectre",20, 13 )
pokemon.information()'''