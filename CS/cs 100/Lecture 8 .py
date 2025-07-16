'''
def getNegativeNumber():
    num= 55 #as long as it is not negative
    while num>= 0 :
            num = int(input('Enter a negative num :'))
    return num 

print(getNegativeNumber())


def getNegativeNumber():
    num= 55 #as long as it is not negative
    while num>= 0 :
            num = int(input('Enter a negative num :'))
            if num <0:
                return num
"da lo mismo que lo de arriba"


print(getNegativeNumber())


def getNegativeNumber():
    num= int(input('Enter a negative num :'))
    while num>= 0 :
        num = int(input('Enter a negative num :'))
    return num
"da lo mismo que lo de arriba"

print(getNegativeNumber())



def getNegativeNumber2():
    while True:
        num= int(input("Enter a negative number"))
        if num <0:
            return num
                 
print(getNegativeNumber2())

#--------------------------------------------------------------->

def hello():
    while True: #always true , si es que se le pusiera while fase, no se imprimir'ia nada
        name=input("What is your name?")
        print("hello{}".format(name))

hello()

def hello():
    while False: #always true , si es que se le pusiera while fase, no se imprimir'ia nada
        name=input("What is your name?")
        print("hello{ }".format(name))

print(hello())

#---------------------------------------------------------------->

def cities():
    lst=[]
    while True:
        city = input("Enter city:")
        if city == '':
            return lst
        else:
            lst.append(city)
print(cities())

def cities2():
    lst=[]
    city=input("Enter your city2: ")
    if city == ' '
        break
    lst.append(city)
    return lst
print(cities2())
'''

def getAges(letter):
    rtnLst=[]
    while True:
        name=input("Enter name :")
        if name== '':
            return rtnLst
        if name[0] != letter:
            continue
        age=int(input("Enter your age : "))
        rtnLst.append(age)

print(getAges('J'))


#----------------------------------------------------->

def all(tabe):
    for row in table:
        for num in row:
            print(num, end='')
        print()

t = [[2,3,0,6],
    [[0,3,4,5],
    [4,5,7,0]]


all(t)

def before (table):
    for row in table:
        for num in row:
            if num==0:
                break
            print(num, end=' ')
        print()


t = [[2,3,0,6],
    [[0,3,4,5],
    [4,5,7,0]]

before(t)
     

    
def before (table):
    for row in table:
        for num in row:
            if num==0:
                continue
            print(num, end=' ')
        print()


t = [[2,3,0,6],
    [[0,3,4,5],
    [4,5,7,0]]

before(t)
     

    
def ignore (table):
    for row in table:
        for num in row:
            if num==0:
                continue
            print(num, end=' ')
        print()


t = [[2,3,0,6],
    [[0,3,4,5],
    [4,5,7,0]]

ignore(t)
     

#-------------------------------
while True:
    print()
    break() #makes no sense on a loop, puts you out of the loop, mientras continue hace skip lo que falta, el codigo de abajo que sobra. 
    print()
    

