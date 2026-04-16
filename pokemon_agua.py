from pokemon import Pokemon

class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        
    def atacar(self, oponente): 
        if self.energia_actual < 15:
            print("NO HAY SUFICIENTE ENERGIA")
            return
        
        self.energia_actual -= 15
        return 15 

from pokemon_fuego import PokemonFuego 
if isinstance(oponente, PokemonFuego):
    golpe *= 2
    print("ES EFECTIVO EL ATAQUE")

    oponente.recibir_golpe(golpe)