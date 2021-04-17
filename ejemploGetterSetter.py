#Este es un ejmplo de como funcionan Getter y Setter

class claseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None #Este __propiedad_privada es un atributo de uso interno, nadie fuera de la clase puede acceder a el, es un atributo de uso interno
        
    def setpropiedadPrivada(self, valor): #Este es un metodo especifico para poder modifciar el atributo privado propiedad_privada desde fuera, utilizando el metodo setter
        self. __propiedad_privada = valor
        
    def getpropiedadPrivada(self): #Este es un metodo getter
        return self.__propiedad_privada
        
    def propiedadPrivada(self, valor=None):
        if valor == None:
            #Actua como getter
             return self.__propiedad_privada
        
        else:
            #Actua como setter
            self.__propiedad_privada = valor
    
    
    
    def __str__(self):
        return "claseConGetterySetter con propiedadPrivada -> {}".format(self.__propiedad_privada)

if __name__ == '__main__':
    c = claseConGetterySetter()
        