excuse= 'I\'m sick'# se le arregla poniendo \
hour=12
minute=37
second=45
print(hour+':'+minute+':'+second)

#si es que hay un int antes de un +, significa que es un operado aritmeticoo
#para arreglarlo, tenemos que definirlo como str a cada uno. 
print(str(hour)+':'+str(minute)+':'+str(second))
infile=open('sample.txt')#----> sino se le pone el rt, python no lo considera error, el problema
#ser'ia que si es que no se le pone el directorio, como especificado. Python considera que ese archivo se encuentra e el mismo directorio del progarma de python.
m=(3+4]#----> no tienesentido como termina la linea, ser'ia un Syntax
if x==5 #le faltar'ia los dos puntos
print 'hello'#----> faltan parentesis
lst=[4;5;6]#---> se tienen que poner comas

for i in range(10):
print(i) #---> aqu'i el problema es la sangr'ia

num=int('4.5')#--> es un float, no un int, es un value error, significa que algo no cuadra.
num=int(4.5)#esto ser'ia lo cprrecto
num=int(float('4.5'))


val=input('enter a number: ')
num=int(val) #aqu'i el rpblema es que aqu'i nosotros no podemos controlar lo que el usuario escrciba. mejor dicho la manera de como escriba el nro, ya sea por letras o solo por numeros


print(3/0)#imposible, infitio la vrdddd

lst=[12,13,14]
print(lst[3])#out of range, 


lst=[12,13,14]
print(lst*3)#si se puede multiplicar int times a list


lst=[12,13,14]
print(lst*lst)#--->type error , porque solo se multiplica int times a list, nada m'as


'''memorizar las slides, y los exception types'''

strAge=input('enter your age')
intAge=int(strAge)
print('you will be {} years old next year.'.format(intAge+1))

#para poder fix el error que el usuario lo ponga en letras o en float en lugar de n'umeros,hacemos lo siguiente.

try:
    strAge=input('enter your age')
    intAge=int(strAge)
    print('you will be {} years old next year.'.format(intAge+1))

except:
    print('i need digits!!')
print('After that code...')
#a penas se encuentre el error, p=el codigo para y procede a imprimir lo que est'a en el cuerpo de except.

def readAge(filename):
    try:
        infile = open(filename)
        strAge = infile.readline()
        age = int(strAge)
        print('Next year you will be', age+1)
    except ValueError:
        print('Value cannot be converted to integer.')
    except FileNotFoundError:
        print('Input file is missing:')
readAge('inputfile.txt')

'''poner atencion a este'''

def readAge(filename):
    try:
        infile = open(filename)
        strAge = infile.readline()
        age = int(strAge)
        print('Next year you will be', age+1,name)#---> aqu'i como est'a este name, y no est'a defone, hay que definirlo porque seria un name error y el programa crash literalmente.
    except ValueError:
        print('Value cannot be converted to integer.')
    except FileNotFoundError:
        print('Input file is missing:')
readAge('inputfile.txt')

#---------> fix it
def readAge(filename):
    try:
        infile = open(filename)
        strAge = infile.readline()
        age = int(strAge)
        print('Next year you will be', age+1,name)
    except ValueError:
        print('Value cannot be converted to integer.')
    except FileNotFoundError:
        print('Input file is missing:', "'" + filename + "'")

readAge('inputfile.txt')
