import math


class Point: #despues de esto se da un comentario, docstring
    #x=0#---> estes es el x self, para que se quede en el codigo guardado el valor de x 
    def __init__(self,x,y): #solo se utiliza para crear un nuevo object
        self.x=x
        self.y=y
    def coordinates(self):#practicamente pregunta por el par ordenado de x y y 
        return (self.x, self.y) #---> siempre con parentesis para que nos devuelva un tupple
    def move_to (self,x,y):#hace replace el old value de x y y que ahora es 7,7
        self.x=x
        self.y=y
    def move(self,x,y):#la dif con el move to es que practicamanete el 7,7 se va a ir sumando a si mismo 
        self.x+=x
        self.y+=y
    def distance_to(self,otherPoint):

        #aqu'i se importa math
        xdiff=self.x-otherPoint.x
        ydiff=self.y-otherPoint.y
        return math.sqrt(xdiff**2+ydiff**2)


p1=Point(5,5)
p1.move_to(7,7)
p1.move(7,7)
p2=Point(8,9)
print(p1.coordinates())
print('distance es:', p1.distance_to(p2))



#otra manera
import math


class Point: #despues de esto se da un comentario, docstring
    #x=0#---> estes es el x self, para que se quede en el codigo guardado el valor de x 
    def __init__(self,x,y): #solo se utiliza para crear un nuevo object
        self.x=x
        self.y=y
    def coordinates(self):#practicamente pregunta por el par ordenado de x y y 
        return (self.x, self.y) #---> siempre con parentesis para que nos devuelva un tupple
    def move_to (self,x,y):#hace replace el old value de x y y que ahora es 7,7
        self.x=x
        self.y=y
    def move(self,x,y):#la dif con el move to es que practicamanete el 7,7 se va a ir sumando a si mismo 
        self.x+=x
        self.y+=y
    def distance_to(self,otherPoint):

        #aqu'i se importa math
        xdiff=self.x-otherPoint.coordinates()[0] #esta es la mejor manera, le cambiamos x por coordinates, para proteger las varibales.
        
        ydiff=self.y-otherPoint.coordinates()[1]
        return math.sqrt(xdiff**2+ydiff**2)


p1=Point(5,5)
p1.move_to(7,7)
p1.move(7,7)
p2=Point(8,9)
print(p1.coordinates())
print('distance es:', p1.distance_to(p2))
