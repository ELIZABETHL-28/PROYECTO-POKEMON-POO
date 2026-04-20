from pokemon import Pokemon

class PokemonPlanta(Pokemon):

    def atacar(self, enemigo):
        if self.energia_actual < 15:
            print("NO HAY ENERGIA SUFICIENTE")
            return

        self.energia_actual -= 15
        golpe = 15

        from pokemon_agua import PokemonAgua
        if isinstance(enemigo, PokemonAgua):
            golpe *= 2
            print("¡EL ENEMIGO FUE PARALIZADO!")

        enemigo.recibir_golpe(golpe)