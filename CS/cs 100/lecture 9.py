
#Lecture 9:

'''infile =open('\somedir\somefolder\example.txt','rt')

infile =open('../folder/example.txt','rt')#-------> lo mismo que lo de arriba. Manera más rápido abajo.

infile =open('example.txt','rt')'''

hdList = ['Humpty Dumpty sat on a wall.',
          'Humpty Dumpty had a great fall.',
          "All the king's horses and all the king's men",
          "Couldn't put Humpty together again!"]

lunaFile = open('luna.txt', 'wt')

for line in hdList:
    lunaFile.write(line+'\n')#el \n significa line+ otra linea de codigo. Funciona como un enter. The new line character es unicamente used por los autores, no afecta el character del line.

lunaFile.close() #tiene que cerrarse, con el nombre de la variable a la cual se le asignó el open. Ahora sale el humpty file ahí en el repositorio de codigo cs

''' el txt es más para organizar de mejor manera, porque si se le pone .py de python, la computadora lo leerá como documento python y van a haber errores por comillas o whatever que el texto tenga.'''



lunaFile=open('luna.txt','r')
for line in lunaFile:
    print(line)#va a salir con espaciado entre cada l'inea


lunaFile=open('luna.txt','r')
for line in lunaFile:
    print(line, end='')#para quitarle el espaciado 


lunaFile=open('luna.txt','r')
line=lunaFile.read(5)
print(line)


lunaFile=open('luna.txt','r')
line=lunaFile.read()#lo lee a todo el file
print(line,end='')
lunaFile.close()


lunaFile=open('luna.txt','r')
line=lunaFile.readline()#lee desde donde se quedó y lo imprime
print(line,end='')
lunaFile.close()

lunaFile=open('luna.txt','rt')
line=lunaFile.readlines() #nos da un lst of strings, hace split y se ve así ----->['Humpty Dumpty sat on a wall.\n',
                          #'Humpty Dumpty had a great fall.\n', "All the king's horses and all the king's men\n", "Couldn't put Humpty together again!\n"]
print(line,end='')
lunaFile.close()

lunaFile=open('luna.txt','r')
for i in range(5):
    line=lunaFile.readline()
    print(line,end='')
lunaFile.close()

#write expects an string.

infile=open('luna.txt','rt')
print(infile.read(1), end='')#read first letter of the file
print(infile.read(5), end='')
print(infile.readline(),end='')
print(infile.read(),end='')#va a leerlo, all the way to the end, desde donde se qued'o obv

infile.close() #SIEMPRE CERRARLO!!!!

#--------------------------------------------------------------------------------------------------
#ESTE ES PARA ESCRIBIR UNA FUNCIÓN

def numwords(filename):
    infile =open(filename)
    content=infile.read()
    infile.close()
    wordList =content.split()
    return len(wordList)

print(numwords("luna.txt")) #o tb---> file=" luna.txt" print(numWord(file))


def numwords(filename):
    infile =open(filename)
    content=infile.read()
    infile.close()
    wordList =content.split()
    return wordList

print(numwords("luna.txt"))


def numLines(filename):
    infile =open(filename,'rt')
    lineList=infile.readlines()
    infile.close()
    wordList =content.split()
    return len(lineList)

print(numwords("luna.txt"))

def numChars(filename):
    infile=open(filename,'rt')
    content= infile.read()
    infile.close()
    return len(content)
file= "luna.txt"
print(numChars(file))

def numChars(filename):
    infile=open(filename,'rt')
    content= infile.read()
    infile.close()
    return content

file= "luna.txt"
print(numChars(file))

outfile = open('test.txt','wt')
outfile.write('T')
outfile.write('his is the first line.')
outfile.write('Still the first line...\n')
outfile.write('Now we are in the second line.\n')
outfile.write('Non string value like' + str(5)+ 'must be converted first.\n')
outfile.close()










