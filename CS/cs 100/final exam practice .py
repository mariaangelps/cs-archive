'''
pregunta 1:
type error porque se est'a sumando lst con lst y de ah'i una lst.

si es que hay dos puntos, es lista, EL RETURN ES UNA LISTA.

pregunta 2:

el output es 6 porque no hay return

prehunta 3: class Point
pregunta 4:
es 4 porque desaparece el nu,=fun(F) y las dem'as tb despues de laa primera.

pregunta 5:

(data o attributes) and (behavior o function)= encapsulation
pregunta 6:  6,6,6,6
la nparte de num=funI(num) y las dem'as siempre desaparecen en una nube de pf

pregunta 8:
es llll sin la lst.

SIN EMBARGO SI:

lst = ['h','e','l','l','o']

lst2 = []

for el in lst:
    lst2.append(el)

print(lst2[2:3]*4) '''#----> AH'I SI SE REGRESA ['L'L'L'L]

'''
Pregunta 9: igual como las anteriores, pero date cuenta que ah'i si hace el print despues de haber umado el +=2

Pregunta 10:

local variable es a=7, la forma  de verlo es el a=7 es dentro del black box, y cuando
se dice que se imprima 4 por 7 y de ah'i espacio a, la a vendr'ia a ser 0, porque solo el 28 est'a dentro del black box.

pregunta 12:
como no est'a la a dentro del black box, python se va para atr'as y ve desde afuera
desde una manera m'as global que numero se le asigna a a.

Question 13:
se imprimen las strings unicamente. ejem contrario al anteiror.

Question 14:
Cuando se refiere a A como global dentro del black box, lo que significa es que
lo que se imprime es 28,8 porque el valor debajo del global va a ser el numero que se va a quedar como declarado, y va a reemplazar el 0 en este caso.

Question 16:
IMPORTANTE!!!!!

the name of the exception raised when a program operation or
function has an argument of the right type but incorrect value?
-ValueError

Question 18:

TypeError:  name of the exception raised when a program operation or function
is applied to an object of the wrong type?

Question 19:

linea 3: porque no existe, filenotfoundererror
linea 5: value error

Question 20:
True porque there are no limits.

Question 22:

A value can be an int
Key Restrictions: 1. Can be any python type that is inmutable. 2. It has to be unique
1ra pregunta: is that a key in the dctionary(two)? practicamente, se intenta sacar el valor dentro de ese key

Question 24:
'tabby' Porque c est'a en cat, entonce se devuelve el valor de cat.
question 26:
update es el nuevo append de dictionaries

Question 26:

SI ES QUE SE HACE ESO, SOLO SE RETPORNAA TWAIN MARK.

def myFunction(d):
    d2 = {'Twain':'Mark'}
    d.update(d2)
    return d2

d = {1:'for the money', 'two':'for the show'}
print(myFunction(d))



TB QUE PASA SI SE HACE ESTO?

def myFunction(d):
    d2 = {'Twain':'Mark'}
    d.update(d2)
    return d2

d = {1:'for the money', 'two':'for the show'}
print(myFunction(d))def myFunction(d):
    d2 = {'Twain':'Mark'}
    d.update(d2)
    return d

d = {1:'for the money', 'two':'for the show'}
print(myFunction(d))

EL OUTPUT SERIA TWAIN MARK, 1 FOR THE MONEY AND TWO FOR THE SHOW, REVISA ESTE MARIA ANGEL


Question 27:
call the name of the class with the arguments you would pass to the
init method.call the name of the class with the arguments you would pass
to the init method. |
                    ^


class Point:
 "'
 def__init__(self,x,y)

 p1=Point(5,7)

Question 28:
Ver que pasa si le pones continue en vez de break????!!!!

Question 30:
A data member of a class= a variable of a class
 assigning a value in a member function using "self."
 assigning a value to a variable declared directly in the class without "self".

'''
#PRESTAR ATENCION A ESTE!!!!!
'''
question 31:

def myFunction(aStr):
    result = (aStr.split()) #sin len
    return result

exclamation = "As easy as 123   " #tres espacios
print(myFunction(exclamation))
rta: igual es 4


def myFunction(aStr):
    result = len(aStr.split(' '))
    return result

exclamation = "As easy as 123"
rta: 4

'''
# mira este
'''
def myFunction(aStr):
    result = len(aStr.split())
    return result

exclamation = "As easy as 123   "
rta: aqui seria 7, porque cuenta los espacios, y le pone las comillas.

question 32:
cuando se vea un while true: lo primero que tiene que tener es un break o un continue o un return.

question 33:
read sin argumento, lee string? ver bien


question 35:
comparar strings de length, se ve por diccionario, como i es mayor a l, pail es mayor a pale en efecto!

question 38:
__init__
self
self.x
x_coor

question 39:
filename
int
ValueError
FileNotFoundError
filename
Question 40:
input:6 porque ceunta los espacios 


 
