from pokemon import Pokemon

class PokemonFuego(Pokemon):

    def atacar(self, enemigo):
        if self.energia_actual < 15:
            print("NO HAY ENERGIA SUFICIENTE")
            return

        self.energia_actual -= 15
        golpe = 15

        
        from pokemon_planta import PokemonPlanta
        if isinstance(enemigo, PokemonPlanta):
            golpe *= 2
            print("¡EL ENEMIGO FUE PARALIZADO!")

        enemigo.recibir_golpe(golpe)