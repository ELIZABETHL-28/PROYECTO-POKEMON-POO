class Pokemon():
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.__nombre = nombre
        self.__hp_actual = hp_maximo
        self.__hp_max = hp_maximo
        self.__energia_actual = energia_maxima
        self.__energia_max = energia_maxima
        
    @property
    def nombre(self):
        return self.__nombre 
    
    @property
    def  hp_actual (self): 
        return self.__hp_actual
    
    @ hp_actual.setter
    def hp_actual(self, valor): 
        if valor < 0: 
            self.__hp_actual = 0
        else: 
            self.__hp_actual = valor
            
    @property
    def energia_actual(self): 
        return self.__energia_actual
    
    @ energia_actual.setter
    def energia_actual(self, valor): 
        if valor < 0: 
            self.__energia_actual = 0
        else: 
            self.__energia_actual = valor               
    
    
    
        

