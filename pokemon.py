class Pokemon():
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.__nombre = nombre
      
    @property
    def nombre(self):
        return self.__nombre   
        
