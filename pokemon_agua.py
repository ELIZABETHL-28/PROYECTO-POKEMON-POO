from pokemon import Pokemon
from pokemon_fuego import PokemonFuego

class PokemonAgua(Pokemon):

    def atacar(self, enemigo):
        if self.energia_actual < 15:
            print("NO HAY ENERGIA SUFICIENTE")
            return

        self.energia_actual -= 15
        golpe = 15

        if isinstance(enemigo, PokemonFuego):
            golpe *= 2
            print("¡EL ENEMIGO FUE PARALIZADO!")

        enemigo.recibir_golpe(golpe)
