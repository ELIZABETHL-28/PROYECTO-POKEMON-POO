class Pokemon:
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self.energia_maxima = energia_maxima
        self.__hp_actual = hp_maximo
        self.__energia_actual = energia_maxima
        self.defendiendo = False
        self.paralizado = False

    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self.__hp_actual = 0
        elif valor > self.hp_maximo:
            self.__hp_actual = self.hp_maximo
        else:
            self.__hp_actual = valor

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self.__energia_actual = 0
        elif valor > self.energia_maxima:
            self.__energia_actual = self.energia_maxima
        else:
            self.__energia_actual = valor

    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            print(self.nombre, "PREPARANDO PARA DEFENDERSE")
        else:
            print("NO HAY ENERGIA SUFICIENTE")

    def descansar(self):
        self.energia_actual += 20
        print(self.nombre, "RECUPERANDO ENERGIA")

    def recibir_golpe(self, golpe):
        if self.defendiendo:
            golpe //= 2
            self.defendiendo = False
            print("EL DAÑO FUE REDUCIDO")

        self.hp_actual -= golpe
        print(self.nombre, "RECIBIO", golpe, "DE DAÑO")            
    
        
    
    
        

