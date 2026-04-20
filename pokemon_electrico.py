from pokemon import Pokemon
import random

class PokemonElectrico(Pokemon):

    def atacar(self, enemigo):
        if self.energia_actual < 15:
            print("NO HAY ENERGIA SUFICIENTE")
            return

        self.energia_actual -= 15
        golpe = 15
        enemigo.recibir_golpe(golpe)

        if random.randint(1, 100) <= 20:
            enemigo.paralizado = True
            print("¡EL ENEMIGO FUE PARALIZADO!")
