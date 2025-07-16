books = ('math', 'physics', 'chemistry', 'history')
c = []
c.append('filosofia')
print(c)
#el output is going to be filosofia, se reemplaza, y como si es lista, se convierte en una totalmente nueva.


x=len("la mama de luis")
print(x) #va a ser 15, en len solo se cuentan las letras y los espacios, nada mas, se cuenta desed 1 


x= ()
r='rock'
c='climbing'
res=r+c
print(res)

#va a salir rockclimbing unido porque no hay separador, el + est'a actuando como union de esos dos caraceteres
# si se le pusiera r,c --> el resultado ser'ia un tuple con str adentro, 


y= "mi mama me mima"
c=y.count("mama")
print(c)

# el output va a ser 1 porque el count indica que unicamente el contador muestre cuantas veces se cumple la funcion que se le est'a dando. 

a = 'tree'           
b = 'truck'
c = a > b
print(c)
#el output ser'ia false, porque no se pueden comparar strings que no seas iguales, a menos que se utilice el metodo len()



a = 'truck'
b = 'truck'
c = a == b
print(c)
#el output ser'ia true por lo que si son ifuales

#ahora en cambio, si es que yo escribo dos strings distintas pero comparo el length entre esas dos, el resultado ya ser'ia un numero

books = ['math', 'physics', 'chemistry', 'history']

c = len(books) + len(books[0])
print(c)


a = ['one', 'in', 'a', 'million']
b = ['time', 'flies', 'swiftly']
c = b[0:1] + a[0:1]
print(c)


lst = ['M','a','r','c','h']
lst2= [ ]
for letter in lst:
    lst2.append(letter)
    print(letter, end='_')
