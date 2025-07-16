

def myAbs(num):
    if num<0:
        return -num
    else:     #explicit else
        return num   
x=-9
print(myAbs(x))



def myAbs(num):
    if num<0:
        return -num     #implicit else 
    return num 
x=-9
print(myAbs(x))

# ESTE ESTUDIAR, VA A ESTAR EN EL EXAMEN

def myMax (inLst): #TITLE
    currentMax = -10000000 
    for current_One in inLst:#HEADER
        if current_One > currentMax: #
            currentMax = current_One #BODY, OF A COMPLEX LINE
    return currentMax

myList = [4,1,9,5,2,-1,15]
print(myMax(myList))



def myMax (inLst): #TITLE
    currentMax = inLst[0]
    for current_One in inLst:#HEADER
        if current_One > currentMax: #
            currentMax = current_One #BODY, OF A COMPLEX LINE
    return currentMax


def myMin (inLst):
    currentMin =  inLst[0]
    for currentOne in inLst:
        if currentOne <currentMin:
            currentMin = currentOne
    return currentMin
        
        
myList = [4,1,9,5,2,-1,15]
print(myMin(myList))



def myLen (inSeq):
    counter = 0
    for i in inSeq:
        counter +=1
    return counter

myList = [4,1,9,5,2,-1,15]
print(myLen(myList))



"how many odd numbers do we have in our list"

def countOdd(inSeq):
    counter = 0
    for i in inSeq:
        if i%2 ==1:
            counter+=1
    return counter

myList = [4,1,9,5,2,-1,15]
print(countOdd(myList))



"how many odd numbers do we have in our list"

def countOdd(inSeq):
    counter = 0
    for i in inSeq:
        if i%2 !=1:
            counter +=1
    return counter

myList = [4,1,9,5,2,-1,15]
print(countOdd(myList))

"how many odd numbers do we have in our list"

def countOdd(inSeq):
    counter = 0
    for i in inSeq:
        if i%2 ==0:
            counter +=1
    return counter

myList = [4,1,9,5,2,-1,15]
print(countOdd(myList))


def mySum (inSeq):
    total =0
    for elem in inSeq:
        total +=elem
    return total


myList = [4,1,9,5,2,-1,15]
print(mySum(myList))


" REvisar esta"

def mySumofOdd (inSeq): #output 1.9.15,5,-1
    total =0
    for elem in inSeq:
        if elem %2!= 0:
            total += elem
    return total

def myLen(inSeq):
    counter=0
    for thing in inSeq:
        counter+= 1
    return counter 


myList = [4,1,9,5,2,-1,15]
s = 'hello, world' #tiene que salie 12, porquee el espacio tb es un character
tup=('hello', 2,5.2, True, ['bye',5])#5 elementos 
print(myLen(tup[4[0]])) #ouptut ser'ia 2, cuenta cada cuantas palabras tiebe cada palabra

myList = [4,1,9,5,2,-1,15]

def myMax (inseq):
    myMax = inseq[0]
    for char in inseq:
        if char>myMax:
            myMax=char
    return myMax


    s=('hello','bye','hi','boo','happy')
    print(myMax(s))



def myMax (inseq):
    myMax = inseq[0]
    for char in inseq:
        if char>myMax:
            myMax=char
    return myMax

s=('been', 'bean')
print(myMax(s))


def countVowels (inStr):
    counter = 0
    vowels ='aeiouAEIOU'
    for letter in inStr:
        if letter in vowels:
            counter +=1
    return counter

s='When in the course of human events '
print(countVowels(s))


def countVowels (inStr):
    counter = 0
    vowels ='aeiouAEIOU'
    for letter in inStr:
        if letter not in vowels and letter != ' ':
            counter +=1
    return counter



s='When in the course of human events '
print(countVowels(s))


def countWowels(inSeq):
    vowels = 'aeiouAEIOU'
    counter = 0  #que pasa si este lo pongo debajo del for? deberia salir un 2 
    for word in inSeq:
        for letter in word:
            if letter in vowels:
                counter +=1
        print(counter)
    return counter



s=['When' ,'in', 'the' ,'course','of',' human', ' events ']
print(countVowels(s))






def countWowels(inSeq):
    vowels = 'aeiouAEIOU'
    lst=[]
    for word in inSeq:
        counter = 0 
        for letter in word:
            if letter in vowels:
                counter +=1
        lst.append(counter)
    return lst 



s=['When' ,'in', 'the' ,'course','of',' human', ' events ']
print(countVowels(s))





