from pokemon_agua import PokemonAgua

animal = PokemonAgua("Squirtle", 80, 50)

print(animal.nombre) 
print(animal.hp_actual)

animal.hp_actual -= 100

# EN LA CLASE DE POKEMON TENEMOS QUE VER Y HACER UNA CLASE ABSTRACTA, Y TENGO QUE VER EN CUAL 
# ME QUEDA MEJOR. 

animal.defender()
animal.recibir_golpe(20)
print(animal.hp_actual)


# # from pokemon import Pokemon

# class PokemonAgua(Pokemon):
#     def __init__(self, nombre, hp_maximo, energia_maxima):
#         super().__init__(nombre, hp_maximo, energia_maxima)