#dictionary allows to
#'first': 1 <----es un solo valor

d={'first': 1,'second':2, 'third':3}
print(d['first'])

definitions = {'modest':'unassuming', 'eat':'chew and swallow'}
bdays = {'Napoleon':'15 Aug 1769', 'Lady Gaga':'Mar 28 1986'}
species = {'Fido':'dog', 'Finny':'catfish', 'Pepe Le Pew':'skunk'}

print(definitions['eat'])#----> debe salir chew and swallow
#con dictionaries solo se accede por el key, mas no por el index, posición del elemtno.

#A value on a dictionary puede ser lo que sea, nr, letra, caracter, lo que sea,
#PERO que este sea inmutable .

#Si por ejemplo, hay dos key, con valores distintos, python siempre va a tomar el 'ultimo.

# EJEMPLO: hola={'Fido':'dog', 'Fido':'catfish'}---> se va a imprimir catfish

d={}
d['CC']= 'computing'

print(d)
print(d['CC'])#--->  Si se le pone solo lo que queremos que se imprima, va a salir computing.

d['CC'] = 'Ying Wu college of Computing'
print(d) #----> va a salir todo
print(d['CC']) #---> Solo va a salir lo del college

whatIsCC= d.pop('CC')#-----> remove the value and print it, va a quedar {} vac'io

print(whatIsCC)
print(d)

d={1:'for the money','two':'for the show'}
print(1 in d)#----> true false statement, is there a 1 in the dictionary?

print(2 in d)#-----> false, porque no hay ning'un dos .
d2={'Twain':'Mark'}

d.update(d2)#----> es como el append de una lista, para dictionatires es un update
print(d)
print(d2)#esta sigue intacta, solo se le append a otra dictionary.



d = {'tree':'oak', 'fish':'guppy', 'dog':'boxer', 'cat':'tabby'}
for thing in d.keys():
    if 't' in thing:
        print(thing, end=' ')#----> tree _espacio ,cat_espacio

    

d = {'tree':'oak', 'fish':'guppy', 'dog':'boxer', 'cat':'tabby'}


for thing in d.keys():#---> tb solo puedo poner for i in d:
    if 't' in d[thing]:
#specify the variable,para que se imprima el valor dentro del key. 
        print(d[thing], end=' ')#----> tabby 


d = {'tree':'oak', 'fish':'guppy', 'dog':'boxer', 'cat':'tabby'}
for values in d.values():#----> d.values, aqu'i exqamina los valores de cada variable, tipo lo que est'a despues de los dos puntos
    if 'y' in values:
        print(values, end=' ')#----> guppy abd tabby

'''order doesnt matter'''

d={}
for i in range (10000000):
    d[i] =str(i)
print(d[5000000])#el output ser'ia 500000, es muy efficient. PREGUNTA DE EXAMENId = {intList: "some int's"}

intList=(1,2,3) #---> si tuviera lista, no funciona 
d = {intList: "some int's"}
print(d[intList])


'''pregunta de examen'''

intList=123 #----> da lo mismo que el anterior 
d = {123: "some int's"}
print(d[123])


grades = [95, 96, 100, 85, 95, 90, 95, 100, 100]

for i in range(100,0,-1):#cuenta al rev'es, de manera decreciente
    if grades.count(i) !=0:
        print(i, ":", grades.count(i))


        
grades = [95, 96, 100, 85, 95, 90, 95, 100, 100]
def frequency(itemList):
    counters = {}
 #{95:1, 96:1,100:1,85:1,95:2,90:1,95:2,100:3,100:4}

    for item in itemList:
        if item not in counters:
            counters[item] = 1
        else:
            counters[item] += 1
    return counters

print(frequency(grades))





'''ejemplo 2:'''

wordOccurrences = [('rabbbit',1),('Alice',1), ('rabbbit',4),('Alice',7),('Alice',10)]
  
def makeIndex(wordPageList):
    wordIndex = {}
 #('rabbit':[1,4] as a single element of the list, 'alice': [1,7,10]
    for item in wordPageList:
        word = item[0]
        page = item[1]
       
        if word not in wordIndex:
            
            wordIndex[word] = [page]
#poner page como una lst, es importante, para poder poner append 
       
        else:
            wordIndex[word].append(page)
    return wordIndex

aliceIndex = makeIndex(wordOccurrences)
print(aliceIndex)




