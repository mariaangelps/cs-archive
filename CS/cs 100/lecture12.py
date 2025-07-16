 #  Lecture 12

 
def double(y):
    x=2
    y*=x #---> significa y = y *x , y de hecho esta linea se va a imprimir segunda pero porque los valores de x y y inicilaes est'an definidos despues de la 2da liena
    
    print('inside double','x= ' ,x,'y= ',y)

    x=3
    y=4
    
x,y=3,4
print('outside double', 'x= ' ,x,'y= ',y)

double(y)#a partir de esto, x sigue siendo 3 y y sigue siendo 4 
print('after douvle','x= ' ,x,'y= ',y)


def g(n):
    print('Start g')
    n+=1
    print('n = ' ,n)

def f(n):
    print('Start f')
    n+=1
    print('n= ',n)
    g(n)

n=1
print('Outside a function,  n = ' ,n)
f(n)
          
def f(b):
    a=6
    return a*b

a=0
print('f(3)= ',f(3))
print('a = ',a)



#PREGUNTA DE EXAMEN

def f(b):
    return a*b
a=0
print('f(3)= ',f(3))
print('a = ',a)
#se va a retornar un cero, porque aun as'i no hay una a dentro de la funcion, python toma el a a fuera, se sale de su sitio local y se va a la parte global.


def f(b)
    global a
    a=6
    return a*b
a=0
print('f(3)= ',f(3))
print('a = ',a) #-----> a ahora va a ser 6, ya no 0



