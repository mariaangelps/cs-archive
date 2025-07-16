
for i in range (2,2): #no va a salir nada, porque empieza en dos y termina en dos, entonces el loop no se da, por lo tanto es 0.
    print(i)

for i in range(2,5):
    print(i)
for i in range(1,6,2): #el dos no va a salir,porque solo cuenta desde el uno hasta el 6, saltandose dos #s , eso es lo que indica el último número
    print(i)
for i in range(0,6,2):
    print(i)
for i in range(10,6,-2):
    print(i)

for i in range(10,8,-2):
    print(i)
for i in range(10,12,-2):
    print(i)

import turtle
t=turtle.Turtle()
t.color('green')
t.width(25)
side=100

for i in range (4):
    print(i) #el numero es las veces que quiero que se haga

    t.forward(side)
    t.left(90)
    #tb puede ser--> for num in range (5,9): y debajo ir'ia la parte del c'odigo
for num in range (5,9,): #es como decir del 5 al 9, cuanto le falta para llegar a tal numero
    print(i)
    t.forward(side)
    t.left(90)

for num in range(0,11):  # for num in range(0,11,-1),---> o solo (11)
    print(num)
for num in range(1,10,-1): #para que se imprima del 1 al 9 contando el 9
    print(num)
for num in range(0,10,2):
    print(num)
for num in range(1,10,2):
    print(num)
for num in range(20,70,10):
    print(num)

for num in range(0,11):  # for num in range(0,11,-1),---> o solo (11)
    if num==10:
        print(num)
    else:
        print(num, end=",")

for num in range(1,10,-1): #para que se imprima del 1 al 9 contando el 9
    if num==9:
        print(num)
    else:
        print(num, end=",")
    print(num)

#------------------------------------------>


start=1
stop=10
step=1
    
for num in range(start,stop,step): #para que se imprima del 1 al 9 contando el 9
    if num==9:
        print(num)
    else:
        print(num, end=" , ")

#----------->
for num in range(start,stop,step): #para que se imprima del 1 al 9 contando el 9
    if num!=stop-step:
        print(num, end=" , ")
     
    else:
        print(num)
        
