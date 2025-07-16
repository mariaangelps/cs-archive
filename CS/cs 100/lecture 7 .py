

"Lecture #7 : "

juliette = "Good night, good night\nParting is such sweet sorrow" #\n, el parting is such a sorrow , va a estar en una new line.

print(juliette)


tabs='col0\tcol1\tcol2' #tabs 
print(tabs)

greeting = "Hello World"
print(greeting[0])

print('hello, world'[0])#----> deber'ia dar lo mismo que un greeting[0], que ser'ia hello.


greeting = "Hello World"
print(greeting[-1])#----> va a dar como resultado la d.
greeting = "Hello World"
print(greeting[1:3])
greeting = "Hello World"
print(greeting[1::1])# ----> se imprime todo menos el primer character
greeting = "Hello World"
print(greeting[-3:-1])#---->rl como output porque empieza al rev'es

abc=['a','b','c']
print(abc[0:2])
print(type(abc[0:2]))

print(abc[0:1])
print(type(abc[0:1]))
print(abc[0])
print(type(abc[0])) #----> va a salir str no lst

print("avocado".index('a')) #misma manera de escribir comon abajo.
#el formati siempre ser;a---> objetco.index('letra dek objecto")
#el output ser'a 2

fruit='avocado'
if '0' in fruit:
    print(fruit.index('0'))

print('s'.isupper())#----> pregunta si tiene uppercase letter, o sea may'uscula.

#-----------------------------------------------------------------------------------------------------------------------------
"Prestar atenci'on a ESTE!!!!"

aStr='my cat is catatonic'
print(aStr.replace('cat','dog'))# astr replace dog por cat; le hace cambios a la copia, o sea al output, mas no al string propio por as'i decirlo. 

newStr =aStr.replace('cat','dog')

print(newStr)
print(aStr)

aStr='my cat is catatonic ' + 'hello'
print(aStr.replace('cat','dog'))# astr replace dog por cat; le hace cambios a la copia, o sea al output, mas no al string propio por as'i decirlo. 

newStr =aStr.replace('cat','dog')

print(newStr)
print(aStr)

newNewStr = 'my cat is catatonic '.replace('cat','dog')
print(newNewStr)#sale---> my dog is dogatonic, esto es legal pero es muy raro que pase esto.Mejor ser'ia escribir el astr.replace

aStr='my cat is catatonic ' 
aStr=(aStr.replace('cat','dog'))#----> la reemplaza con el output,l op sea el outout queda stored en esa variable, lo reemplaza, mas no lo cambia, porque las str sn immutables.
print(aStr)

#----------------------------------------------------------------------------------------------------------------------------------
"STR METHODS LISTA DE LOS MÉTODOS:"

aStr='my cat is catatonic ' 
aStr=aStr.capitalize()#Just capitalize the First letter, O sea la hace mayuscula
print(aStr) 

aStr='my cat is catatonic ' 
aStr=aStr.count('cat')#cuenta cada vez que se repite lo que se le pide que imprima, en este caso, lo que está dentro de los paréntesis.
print(aStr)

aStr='my cat is catatonic ' 
aStr=aStr.count(' cat ')#este va a dar como output solo 1, porque se le cuenta con los espacios, y este hace match con el que más se parece. 
print(aStr)

aStr='my cat is catatonic ' 
aStr=aStr.endswith('nic')
print(aStr)#va a retornar verdadero o falso

aStr='my cat is catatonic ' 
aStr=aStr.startswith('my')
print(aStr) #True

aStr='my cat is catatonic ' 
aStr=aStr.startswith('My')
print(aStr) #False

aStr='my cat is catatonic '
aStr=aStr.capitalize()
aStr=aStr.startswith('My')
print(aStr)#True

aStr='my cat is catatonic '
print(aStr.index('cat'))#va a saler 3, porque esta sale en posicion 3

aStr='my cat is catatonic '
if 'dog' in aStr:
    print(aStr.index('dog'))
else:
    print("not there")


aStr='my cat is catatonic '
print(aStr.find('dog'))# si es que no lo encuentra, devuelve un -1, si es que s'i, funciona como el index.


aStr='my cat is Catatonic '
print(aStr.islower())#return lowercase, o sea minuscula. It takes no arguments, es decir, no tiene nros o letras dentro de los paréntesis.

#--------------------------------------------------------------------------------------------------------------------------------------------------


s=' '
print(s.isspace)

#o tb puede ser

s= ' '
print(s==' ')

s= 'Captain, incoming transmission'
print(s.split()) # lo que hace es separar cada palabra, incluyendo la coma y sin espacios.
s= 'Captain, incoming transmission'
print(s.split()) #dar'ia el mismo output

s= 'Captain, incoming transmission'
print(s.split(', ')) #cuando se le especifica con la coma, esto significa que la coma es el l'imite hasta donde se separa, por lo tanto el output ser'ia "captain", "incoming transmission"


s= "(hello!)"
print(s.strip("()!")) #output hello sin tanta cosa

name=input("enter your name:")

name=name.strip(" ()! ")
if name=="john":
      print('welcome John')
else:
    print("sorry i dont know you!")
          
    

import string
print(string.punctuation)

name= "John"
if name.strip(string.punctuation)=="John":
    print("Welcome")
else:
    print("Go away!")
    
import string


s="How are you sir?'"
words=s.split()
print(words)
print(s)
# tb se puede hacer as'i


s="How are youm sir?"
s=s.strip(string.punctuation)
words=s.split()
print(words)

for word in words:
    print(word.strip(string.punctuation)) #separa las palabras, palabra por palabra en distinta linea

words =[ "Its", "warm", "today","yeah?"]
for word in words:
    temp= ' ' 
    for letter in word:
        if letter not in string.punctuation:
            temp +=letter
    print(temp) #imprimiendo las que no forman parte del punctuation de una string

for word in words:
    hello= ' ' 
    for letter in word:
        if letter not in string.punctuation:
            hello +=letter
    print(hello)

#--------------------------------------------------------------------
content = '''
<?xml version="1.0" encoding="UTF-8"?>
<user>
    <name>admin</name>
    <desc>First account created during the Windows installation.</desc>
    <permissions>Full control of the files and local resources.</permissions>
        
    <secret>
        <key>p@$$w0rd</key>
        <lastChanged>1/1/2020:12:05:00</lastChanged>
    </secret>
</user>
'''
print('First' in content)


start=content.index('<key>') + len('<key>')#<key> se le suma len para contar los caracteres que key tiene. 
end= content.index('</key>')

password = content[start:end]
print(password) #esto para imprimir solo la contraseña


print('pi= ' +str(3.14))

    
def f():
    pass #this line intencionalmente se la deja en blanco
print(f)

word ="hello"
for i in word:
    print(i, end='')
print(1,2,3)
print(1,2,3,sep=': ', end=': ')
        


print(1,2,3,sep='- ', end=':\n')# change the default


print('{} is {}'.format('Big Bird', 'yellow'))#-----> Big Bird is yel print('{} is {}'.format('Oscar', 'grumpy')) ----# Oscar is grumpy


bird ='bif bird'
color='yellow'
print('{} is {}'.format(bird.color))

