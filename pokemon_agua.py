from pokemon import Pokemon

class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        
    def atacar(self, enemigo): 
        if self.energia_actual < 15: 
            print("LA ENERGIA NO ES SUFICIENTE")
            return
        
        self.energia_actual -= 15
        golpe = 15
        
        from pokemon_fuego import PokemonFuego
        if isinstance(enemigo, PokemonFuego): 
            golpe *=2 
            print("FUNCIONA DE MARAVILLA")
            
        enemigo.recibir_golpe(golpe)
        