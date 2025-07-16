

#Lecture 6 

"print() sin el argumento significa que it skips a line, ser'ia un salto de linea"

def iSquaredPlus10(x): # x means a formal parameter 
    result = x**2 +10
    return result

x=5 

result = iSquaredPlus10(x)

    
print(result)  # esta x no es la misma x de arriba

x=1
result = iSquaredPlus10(x)
print(result)

x=3
result =iSquaredPlus10(x)
print(result)    #-----> pyhton returns a value always, sino se devueleve impromiendo la palabra none


x=0
result= iSquaredPlus10(x)
print(result)


def iSquaredPlus10(x):
    result =x**2 +10
    print(result)

x=0
result= iSquaredPlus10(x)

#print(result)#----> si se le pne print luego de la def, y del primer print, se escirbe un none.


def areaofRectangle (a,b): #---> las que est'am entre parentesos, som aquellas que han sido dropped y como no hay return, solo se imprime 
  
    return a*b

length =3
width = 4
print(areaofRectangle(length,width))


'''def areaofRectangle (stupidName1,stupidName2): #---> las que est'am entre parentesos, som aquellas que han sido dropped y como no hay return, solo se imprime
return stupidName1*StupidName2"
length =3
width = 4
print(areaofRectangle(length,width))

def hello (name):
    line="welcome," +name + ", to the world of Pyton."
    return line

print(hello("Julie"))
print(hello(tom))'''


#exercise

def oddCount(inlist):
    counter = 0
    for num in inlist:
       if num%2 != 0:
           counter +=1 #counter = counter+1
        #else:
           # pass #se le pone esto, para que si  no se cumple el statemenet, pues que no pase nada, entonces se escribe pass, es como un blank line
    return  counter   #tener cuidado de no poner el return abajo del if, porque estar'ia incorrecto 

    
numList =[4,0,1,-2]
print(oddCount(numList))



#exercise commenting functions

def oddCount(inlist):
    
    ''' This function should count how many odds in a list.''' #RULE EXAM DOT STRING: MULTILINE COMMENT THREE DOUBLE QUOTES, NO EL NUMERAL # y
    oddCounter =0
    evenCounter=0                                               #tiene que ser la primera l'inea del cuerpo, first part of a body
    counter = 0
    for num in inlist:
       if num%2 != 0:
           counter +=1 #counter = counter+1
       else :
           evenCounter +=1

    return  (oddCounter,evenCounter)   #tener cuidado de no poner el return abajo del if, porque estar'ia incorrecto 

    
numList =[4,0,1,-2,1]
print(oddCount(numList))




