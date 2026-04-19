from pokemon import Pokemon 
import random

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        self.paralizado = False 

    def atacar(self, enemigo): 
        if self.energia_actual < 15:
            print("LA ENERGIA NO ES SUFICIENTE")
            return
        
        self.energia_actual -= 15
        golpe = 15 

        if random.randint(1, 5) == 1: 
            print("EL ENEMIGO ESTA PARALIZADO")
            enemigo.paralizado = True 

        enemigo.recibir_golpe(golpe)