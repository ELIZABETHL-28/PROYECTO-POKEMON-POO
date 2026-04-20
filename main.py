from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_agua import PokemonAgua
from pokemon_fuego import PokemonFuego
from pokemon_planta import PokemonPlanta
from pokemon_electrico import PokemonElectrico
import random 

def crear_pokemon(opcion):
    datos = CATALOGO_POKEMON[opcion]

    if datos["tipo"] == "Fuego":
        return PokemonFuego(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif datos["tipo"] == "Agua":
        return PokemonAgua(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif datos["tipo"] == "Planta":
        return PokemonPlanta(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif datos["tipo"] == "Electrico":
        return PokemonElectrico(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
    
def elegir_accion():
    print("1. Atacar")
    print("2. Defender")
    print("3. Descansar")

    return input("Elige: ")

def batalla(criaturauno, criaturados, modo): 
    turno = 1 

    while cri

mostrar_catalogo_disponible()
opcion = input("Elige tu Pokémon: ")
jugador = crear_pokemon(opcion)
print(f"Elegiste a {jugador.nombre}")

# EN LA CLASE DE POKEMON TENEMOS QUE VER Y HACER UNA CLASE ABSTRACTA, Y TENGO QUE VER EN CUAL 
# ME QUEDA MEJOR.