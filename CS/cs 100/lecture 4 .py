line1= 'Marimar'
line2= 'Costeñita soy  '
line3=20
print(line1)
print(line2)

print(line1,line2) #la coma hace que se cree un espacio 

print(line1+ ' ' +line2+str(line3)) #dos comillas para tener un espacio

s1= line1+ ' ' +line2+str(line3) # Forma #1--> puedo sacar esto de arriba porque no depende del print

print(s1)

s2= (line1, line2) # Forma #2 --->#it would create a tuple,sino se pone los parentesis, pero tb se le puede poner y el output
                   # Va a estar entre paréntesis ()
                
print(s2)

print(0)
print(0.0)
print('zero')
print([0,1,'two'])

print('hello', end= ' maifren ')
print('hello', end= '\n\n\n')#\n significa que el código, se salte de línea, depenede de aucntos n ponga
print('hello', end= '---')
print('hello')


first=input("Enter your first name: ")
last =input("Enter your last name: ")

print( first,last)

name=input("Enter your name: ")
age= input("Enter your age: ")
print(name + " you will be " + str(int(age)+1) + " next year :)" )# Forma#1 para sumar la edad +1, sería, str(int(age)+1)
print(name , " you will be " , int(age) + 1 ,  "next year :)" ) # Forma #2 para sumar la edad +1, sería con comas, y el age
                                                                #iría con un int, para que se lo tome como un valor no, una str .

age1=int(age)+1
print(name , " you will be " , age1 ,  "next year :o" ) #forma #3 


age2=int(input("Enter your age: "))
print(name , " you will be " , age2,  "next year :)" )

age2=int(input("Enter your age: "))
print(name , " you will be " , age2,  "next year :)" )

age += 5 #age =age+1
print(name , " you will be " , age,  "next year :)" )

#---------------------------------------------------



           
nombre=input("Enter your name: ")
edad = int(input("Enter your age: "))
print(edad>=18)

