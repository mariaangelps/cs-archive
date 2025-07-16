
import math
class Point:
    '''Represents a point in a Eucledian plane'''
    x=0
    y=0#----> por el hecho que son dos puntos, y empiezan en 0,0
    def __init__(self,x_coor,y_coor): # son dos guiones bajos, o sea dos veces en izq y derecha---practicamente dos argumentos aqui, x y  y
        x=5
        self.x=x_coor #my x 
        self.y=y_coor #my y

    def coordinates(self):
        '''Return a tuple of the x, y coordinates of a point'''
        return(self.x, self.y)
    def move_to(self,x_coor,y_coor):
        '''Assign new coordinates to a point.'''
        self.x=x_coor
        self.y=y_coor
        
p1=Point(5,7)
print(p1.coordinates())
p1.move_to(10,10)
print(p1.coordinates())





#------------------------->
class Point:
    
    def __init__(self,x_coor,y_coor): # son dos guiones bajos, o sea dos veces en izq y derecha---practicamente dos argumentos aqui, x y  y
        self.x=x_coor #my x 
        self.y=y_coor #my y

    def coordinates(self):
        return(self.x, self.y)
    def move_to(self,x_coor,y_coor):
        self.x+=x_coor #self.x=self.x+x_coor
        self.y+=y_coor
    def move(self,x_coor,y_coor):
        self.x += x_coor
        self.y += y_coor
        
p1=Point(5,7)
print(p1.coordinates())
p1.move(1,-1)#------> sumando by 1 y -1
print(p1.coordinates())

#_--------------->

class Point:
    def __init__(self,x_coor,y_coor): # son dos guiones bajos, o sea dos veces en izq y derecha---practicamente dos argumentos aqui, x y  y
        self.x=x_coor #my x 
        self.y=y_coor #my y

    def coordinates(self):
        '''Return a tuple of the x, y coordinates of a point'''
        return(self.x, self.y)
    def move_to(self,x_coor,y_coor):
        '''Assign new coordinates to a point.'''
        self.x+=x_coor #self.x=self.x+x_coor
        self.y+=y_coor
    def distance_to(self,otherGuy):
        xdiff =self.x-otherGuy.x
        ydiff=self.y-otherGuy.y
        return math.sqrt(xdiff**2+(ydiff*ydiff))
        
p1=Point(3,3)
p2=Point(6,7)
print(p1.distance_to(p2))
#------------------------------->
'''Para importar un punto de la clase se hace as'i'''
'''
import point
p1=point.Point(3,3)
p2=point.Point(6,7)
p2.move(1,1)
print(p1.distance_to(p2))
#---------------------------------->
class Point:
    dimension=0
    def __init__(self,x_coor,y_coor): # son dos guiones bajos, o sea dos veces en izq y derecha---practicamente dos argumentos aqui, x y  y
        self.x=x_coor #my x 
        self.y=y_coor #my y

    def coordinates(self):
        return(self.x, self.y)
    def move_to(self,x_coor,y_coor):
        self.x+=x_coor #self.x=self.x+x_coor
        self.y+=y_coor
    def distance_to(self,otherGuy):
        xdiff =self.x-otherGuy.x
        ydiff=self.y-otherGuy.y
        return math.sqrt(xdiff**2+(ydiff*ydiff))
        
p1=point.Point(3,3)
p2=point.PointPoint(6,7)
print(p1.distance_to(p2))
print(p1.dimension)
print(p2.dimension)


class Point:
    dimension=0
    def __init__(self,x_coor,y_coor): # son dos guiones bajos, o sea dos veces en izq y derecha---practicamente dos argumentos aqui, x y  y
        self.x=x_coor #my x 
        self.y=y_coor #my y

    def coordinates(self):
        return(self.x, self.y)
    def move_to(self,x_coor,y_coor):
        self.x+=x_coor #self.x=self.x+x_coor
        self.y+=y_coor
    def distance_to(self,otherGuy):
        xdiff =self.x-otherGuy.x
        ydiff=self.y-otherGuy.y
        return math.sqrt(xdiff**2+(ydiff*ydiff))
    def getDimension(self):
        return self.dimension
    def setDimension(self,dim):
        self.dimension=dim
        
p1=point.Point(3,3)
p2=point.Point(6,7)
p2.move(1.1)
print(p1.distance_to(p2))
p1.setDimension(5)
print(p1.getdimension())
print(p2.getDimension())'''

#-------------------------------->
#lo que está alado del punto a la derecha, tiene que ser un methodclass Point:

    dimension=0
    def __init__(self,x_coor,y_coor): # son dos guiones bajos, o sea dos veces en izq y derecha---practicamente dos argumentos aqui, x y  y
        self.x=x_coor #my x 
        self.y=y_coor #my y

    def coordinates(self):
        return(self.x, self.y)
    def move_to(self,x_coor,y_coor):
        self.x+=x_coor #self.x=self.x+x_coor
        self.y+=y_coor
    def distance_to(self,otherGuy):
        xdiff =self.x-otherGuy.coordinates()[0]
        ydiff =self.y-otherGuy.coordinates()[1]
        return math.sqrt(xdiff**2+(ydiff*ydiff))
    def getDimension(self):
        return self.dimension
    def setDimension(self,dim):
        self.dimension=dim

'''import point
p1=point.Point(3,3)
p2=point.Point(6,7)
print(p1.distance_to(p2))
p1.setDimension(5)
print(p1.getdimension())
print(p2.getDimension())'''
