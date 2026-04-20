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

def seleccionar_modo(): 
    while True: 
        print("«««««««««««««««««««««««««««««««««««««««««««««")
        print("SIMULADOR DE BATALLAS POKÉMON")
        print("«««««««««««««««««««««««««««««««««««««««««««««")
        print("1 - JUGADDOR VS JUGADOR")
        print("2 - JUGADOR VS COMPUTADORA")

        try: 
            opcion = int(input("SELECCIONE EL MODO A JUGAR: "))
            if opcion == 1 or opcion == 2: 
                return opcion
            else: 
                print("OPCION FUERA DEL RANGO")
        except ValueError:
            print("ENTRADA INVALIDA. DEBE SER UN NUMERO")

# ksdjaksdjalksdak      
def seleccionar_pokemon(nombre_jugador):
    from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible

    mostrar_catalogo_disponible()

    while True:
        try:
            opcion = input(f"{nombre_jugador}, elige tu Pokémon: ")
            if opcion in CATALOGO_POKEMON:
                return crear_pokemon(opcion)
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida.")

# asjdkajsdkajskd
def elegir_accion():
    while True:
        print("1. Atacar (15 EP)")
        print("2. Defender (5 EP)")
        print("3. Descansar (+20 EP)")

        try:
            accion = int(input("Elige una acción: "))
            if 1 <= accion <= 3:
                return accion
            else:
                print("Opción incorrecta.")
        except ValueError:
            print("Entrada inválida.")

# asjdkasdjlkasjdalksda
def ejecutar_turno(pokemon_actual, pokemon_enemigo, es_cpu=False):
    if pokemon_actual.paralizado:
        print(pokemon_actual.nombre, "está paralizado y pierde el turno.")
        pokemon_actual.paralizado = False
        return

    print("-----------------------------------")
    print("Turno de", pokemon_actual.nombre)
    print("HP:", pokemon_actual.hp_actual, "/", pokemon_actual.hp_maximo)
    print("EP:", pokemon_actual.energia_actual, "/", pokemon_actual.energia_maxima)

    if es_cpu:
        accion = random.randint(1, 3)
        print("La computadora elige:", accion)
    else:
        accion = elegir_accion()

    if accion == 1:
        pokemon_actual.atacar(pokemon_enemigo)
    elif accion == 2:
        pokemon_actual.defender()
    elif accion == 3:
        pokemon_actual.descansar()

# sdjakslkdjaslkdjalksjd
def batalla(pokemon_1, pokemon_2, modo):
    turno_jugador_1 = True

    while pokemon_1.hp_actual > 0 and pokemon_2.hp_actual > 0:
        if turno_jugador_1:
            ejecutar_turno(pokemon_1, pokemon_2, False)
        else:
            if modo == 2:
                ejecutar_turno(pokemon_2, pokemon_1, True)
            else:
                ejecutar_turno(pokemon_2, pokemon_1, False)

        turno_jugador_1 = not turno_jugador_1

    print("===================================")
    if pokemon_1.hp_actual > 0:
        print(pokemon_1.nombre, "gana la batalla")
    else:
        print(pokemon_2.nombre, "gana la batalla")


# askldjaskljdalskjdaslkdjdas
modo = seleccionar_modo()

pokemon_jugador_1 = seleccionar_pokemon("Jugador 1")

if modo == 1:
    pokemon_jugador_2 = seleccionar_pokemon("Jugador 2")
else:
    from pokedex import CATALOGO_POKEMON
    opcion_cpu = random.choice(list(CATALOGO_POKEMON.keys()))
    pokemon_jugador_2 = crear_pokemon(opcion_cpu)
    print("La computadora eligió a", pokemon_jugador_2.nombre)

print("¡COMIENZA LA BATALLA!")
batalla(pokemon_jugador_1, pokemon_jugador_2, modo)



# Menú inicial
mostrar_catalogo_disponible()
opcion = input("ELIJE TU POKÉMON: ")
pokemon_jugador = crear_pokemon(opcion)
print("ELEGISTE A: ", pokemon_jugador.nombre)
