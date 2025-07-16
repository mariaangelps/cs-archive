

lst = [1,2.0,'tree', ["hello",2]]


print(lst)

print(lst[0]) # just 1 

print(lst[2])  #single element, va a salir tree

print(lst[2]*2)

print(type(lst[2]*2)) #para saber que tipo es

print(lst[1])

print(lst[3]) #entire list pero de la que est'a adentro del list. Aqu'i, se imprime sin los corchetes---> "hello",2


print(lst[3:4]) #El":" siempre va a ser un listright never gonna reach that, left es el que si se lo incluye. Deber'ia imprimirse as'i, con los corchetes-->["hello",2]


print(lst[-1])#lo mismo que arriba

print(lst[-1][1]) #sacar el dos del -1, un lst de otro lst


print(lst[-1][0]) #sacar el 'hello' del -1, un lst de otro lst

print (lst[-1][0][0]) #sacar la h del hello
print (lst[-1][0][1]) #sacar la e del hello

print (int(lst[1])) # 1era manera de sacar solo el 2 de la lst primera, sin el decimal, sin el float


print(str(lst[1])[0]) # 2da manera de sacar solo el 2 de la lst primera, sin el decimal, sin el float

print(type(str(lst[1])[0]))



# lecture 3

import math
 
print((int(math.sqrt(4))))  #le puse el int para que se quite el decimal

r= 8
print(  3.14*(r**2))     #area of a circle, pir^2
print(math.pi*r**2)    #siempre siempre  math. lo que se pida

import turtle

t= turtle.Turtle()  #turtle object is the pen, it draws from the perspective of the pen, always have to write like this, because it is the turtle constructor

side = 200

s= turtle.Screen() #drawing surface

t.color('cyan') #changes the line color

t.width(10) #10 o cualquier # pixels, grosor del l'apiz



t.forward(side) # ser'ia ir a la derecha
t.left(90) #arrow pointing up, it refers to the angle
t.forward(side)
t.left(90)
t.color('red')#se pintar'ia de rojo una mitad del gr'afico, y la otra mitad cyan



t.forward(side)
t.left(90)

s= turtle.Screen() #drawing surface



t.forward(side)
t.left(90)





