from pokemon_agua import PokemonAgua
from pokemon_fuego import PokemonFuego

criaturauno = PokemonAgua("Squirtle", 100, 50)
criaturdos = PokemonFuego("Charmander", 100, 50)

criaturauno.atacar(criaturdos)
print(criaturdos.hp_actual)

# EN LA CLASE DE POKEMON TENEMOS QUE VER Y HACER UNA CLASE ABSTRACTA, Y TENGO QUE VER EN CUAL 
# ME QUEDA MEJOR.