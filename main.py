import turtle

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    
    def __init__(self, width, height): #Esto es para definir el ancho y la altura de la pantalla que actua como circuito de la carrera
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height) 
        self.__screen.bgcolor('lightgrey')
        self.__startLine = -width/2 + 20
        self.__finishLine = -width/2 - 20
        
        self.__createRunners()
        
    def ___createRunners(self):   
        for i in range(4): #Este bucle lo que hace es crear a los 4 corredorres
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup() #metodo de turtle que levamta el boli y hace que no pinten en su recorrido
            new_turtle.setpos(self.__startLine, self.__posStartY[i]) #esta linea es para centrar a los corredores en la posicion de salida segun lo indicado en los atributos de la class Circuito
            
            
            self.corredores.append(new_turtle)
            

if __name__ == '__main__':
    circuito = Circuito(640, 480)
        