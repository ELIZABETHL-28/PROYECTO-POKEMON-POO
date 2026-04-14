from base import Pokemon

class PokemonAgua(Pokemon):
    def atacar(self, oponente):
        print(f"{self.nombre} lanza un ataque de agua contra {oponente.nombre}")
        daño = 20
        if isinstance(oponente, PokemonAgua): 
            daño *= 2
        oponente.hp_actual -= daño
        