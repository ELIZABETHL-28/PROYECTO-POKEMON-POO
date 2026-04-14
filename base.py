class Pokemon:
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.__nombre = nombre
        self.__hp_maximo = hp_maximo
        self.__hp_actual = hp_maximo
        self.__energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima

    # Propiedades (getters y setters)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, valor):
        self.__hp_actual = max(0, min(valor, self.__hp_maximo))

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, valor):
        self.__energia_actual = max(0, min(valor, self.__energia_maxima))

    # Métodos genéricos
    def atacar(self, oponente):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases hijas")

    def defender(self):
        print(f"{self.__nombre} se defiende y reduce el daño recibido.")

    def descansar(self):
        print(f"{self.__nombre} descansa y recupera energía.")
        self.energia_actual += 10
