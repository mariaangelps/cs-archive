lst =[1,2,3,4]
print(lst[1:])# left start, right stop, xuando el numero vaya antes o bien  depsues de los dos puntos




p1= ['do', 'it', 'better']
p2 =['make', 'us', 'stronger']

print(p1[1]) #with no :, nos dar'a el elemento sin el list, es decir sin los corchetes 

print(p1[1:2]) # si es que tiene los dos puntos, la resppuesta nos dar'a una list

      
print(p1[1:1])

print(p2[0]+p1[1]+p1[2])  #individual strings, el output no va a tener una list, va a salir la palabra make it better pero todo unido


print(p2[0:1]+p1[1:2] +p1[2:3])  #as'i si sale como una list, es el contra ejemplo para arriba

print (p2[0:1]+p1[1:3]) # l'inea mejorada de la de arriba, porque se est'an en la misma l'inea

a=3   #int 
b=3.0  #float
c='three'    #string
d= [1,2,3]   #list

print(type(a)) #clear the object, its like a wrapper, it shows what the variable's type is

print(2**1024)  #pregunta de EXAMEN ---> do INTS have an upper limit? No---> Do floats? yes, they DO have an Upper limit. print(2**1024) sí funciona
                                                                            #pero de ahí si se le pone un decimal, ya sale error---> print(2.0**1024) 


print(3+(5*2))

a= int(3)
b=float(3.0)
c=str('three'  )  
d= list([1,2,3] ) #ALL OF THESE ARE CONSTRUCTORS

n=3
m=5.0
r=n+m
print(r)


n=3
m=5.0
r=n+m
print(r)

n=3
m=5.0
r=n+int(m) #if we put int, the output will not be 8.0, it will be 8 
print(r)

age=20
name='JOHN'
print((name+ ' is ' + str(age))) #here it forces the age variable top be a string, para que se puedan sumar manzanas con manzanas. Str con Str

age=20
name='JOHN'
result= name+ ' is ' + str(age)
print(result)

print(name,'is', age) #cuando se pone coma DENTRO DEL PRINT, tambien es como ponerle el "+" Y se suma lo que est'a escrito


age=20
name='JOHN'
result=  name +' ' +str(age)
print(result)

age='20.0'  #I CANNOT WRITE A FLOAT INSIDE A STRING-----> age='20.0' unless i write an ---> int(float(age))

print(int(float(age)))


fish=['goldfish']   #string inside a list, if we multiply by a number, ots gonna give us the string name the times it was multiplied by.
myPets=['cat','dog']
pets=fish +myPets
print(pets)
print(fish*2)
print('frog' in pets)

pets.append('guinea pig')  #agregar elmentos a la lista 
pets.append('dog')
print(pets)

pets.count('dog')  #how many times the string is in the list

pets.remove('dog')  #grabs the first match of the duplicated element

print(pets)
pets.remove('dog')
print(pets)

import math
print(math. sqrt(4)) #to get a sqrt of a number is by saying---> import math ---> tb se puede escribir in the shell 'help(math)' sin las comillas, y debe salir una lista

import math
print(math.pi)

side1= 3
side2 =4
hyp= math.sqrt((side1**2+ side2**2))
print(hyp==5) # esto se convertiría en un statement de True or False

import math 
r=10
area = math.pi * r**2

print(area)

import math
x= 5
y=5
hyp= math.sqrt((x**2) +(y**2)< r) #le pongo el <r para mostrar que el rsultado debe ser menor a 7

print(math.sqrt((x**2) +(y**2)== r)
print(math.sqrt((x**2) +(y**2)> r)

print(



