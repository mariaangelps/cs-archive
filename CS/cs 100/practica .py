

def puntuacion(alumno1,alumno2,alumno3,alumno4,alumno5):
    suma = alumno1+alumno2+alumno3+alumno4+alumno5
    return suma/3

media =puntuacion(7,8,9,4,6)
print("La puntuacion de esta clase es :" , str(media))

media=puntuacion(9,10,5,3,5)

print("La puntuacion de esta clase es :" , str(media))



def puntuacion(clase):
    return sum(clase)/len(clase)

clase=[7,8,9,4,6]
media =puntuacion(clase)
print("La puntuacion de esta clase es :" , str(media))


clase=[9,10,5,3,5]
media=puntuacion(clase)
print("La puntuacion de esta clase es :" , str(media))



a='tree'
b='truck'
c= a>b
print(c)

name = input('Enter your name: ')

age = int((input('Enter your age: ')))

print(name + ', you will be ' + str(age)+ str(1) + ' next year.')
