from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_agua import PokemonAgua
from pokemon_fuego import PokemonFuego
from pokemon_planta import PokemonPlanta
from pokemon_electrico import PokemonElectrico
import random

def crear_pokemon(opcion):
    datos = CATALOGO_POKEMON[opcion]

    if datos["tipo"] == "Agua":
        return PokemonAgua(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
    elif datos["tipo"] == "Fuego":
        return PokemonFuego(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
    elif datos["tipo"] == "Planta":
        return PokemonPlanta(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
    elif datos["tipo"] == "Electrico":
        return PokemonElectrico(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

# Menú inicial
mostrar_catalogo_disponible()
opcion = input("ELIJE TU POKÉMON: ")
pokemon_jugador = crear_pokemon(opcion)
print("ELEGISTE A: ", pokemon_jugador.nombre)
